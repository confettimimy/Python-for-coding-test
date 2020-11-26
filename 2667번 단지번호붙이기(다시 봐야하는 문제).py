n = int(input())
a = [list(map(int, input())) for _ in range(n)] # 인접 행렬 방식

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # (-1,0) (1,0) (0,-1) (0,1)

ans = [] # 각 단지마다 집의 개수
cnt = 0

# 방문체크용
dist = [[False] * n for _ in range(n)]
print(dist)



def dfs(x, y): # (x, y)는 시작 위치 인덱스
    # 집 개수 증가 & 방문체크
    global cnt
    cnt += 1
    dist[x][y] = True ##### 현재 인덱스 방문처리 해버리고 

    # 인접한 노드 탐색하면서 연결되어 있으면 dfs 재귀호출
    for k in range(4): # 네 방향 모두 한 번씩 확인하면서
        nx, ny = x + dx[k], y + dy[k]

        # 상, 하, 좌, 우 중에서 갈 수 있는 경우
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == 1 and dist[nx][ny] == False:
                dfs(nx, ny) ##### 연결된 곳도 dfs 재귀 수행해서 또 방문처리 -> 아래 함수 모든 정점 확인 이중 포문에서는 이미 연결된 곳으로 간과됐으니 다른 새로운 시작점을 찾을 수 있는거임.



# 모든 정점을 확인해서 시작점이 될 수 있는지 확인. 시작점이 가능하면 dfs 탐색 GO
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and dist[i][j] == False: #####
            print('(',i,',',j,')') # 시작점이 될 수 있는 인덱스 위치 확인용
            
            cnt = 0
            dfs(i, j) # cnt개수가 원래 0이였다가 dfs함수 호출 후 값이 집개수(한 단지 당)로 세팅돼 있을거임.
            ans.append(cnt)



print(len(ans))
ans.sort()
print('\n'.join(map(str, ans)))
