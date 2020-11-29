# 전역변수 개념 다시보기(  )


# 방향배열 ('대각선상에 집이 있는 경우는 연결된 것이 아니다'라는 문제조건 때문에 상하좌우만)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] # (-1,0) (1,0) (0,-1) (0,1)

ls = [] # 각 단지에 속하는 집의 수
home_cnt = 0 #####

def dfs(x, y): # (x, y)는 시작 위치 인덱스
    visited[x][y] = True # 현재 인덱스 방문처리 해버리고 
    global home_cnt ##### 아마 파이썬에서는 전역변수 값 수정이 불가한데 수정 시 global을 써주면 되는 것으로 알고있다.
    home_cnt += 1

    # 인접한 노드 탐색하면서 연결되어 있으면 dfs 재귀호출
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and maps[nx][ny] == 1:
            dfs(nx, ny)
            # 연결된 곳도 dfs 재귀 수행해서 또 방문처리
            # 스택, 재귀와 같은 모습으로 시작점과 연결된 곳들은 쭉쭉 탐색, 방문처리하며 가게 될 것임.
            # 아래의 모든 정점 확인 이중 포문에서는, 시작점과 연결된 모든 노드들은 윗줄 말대로 방문처리되어 이미 연결된 곳들로 간과될 것 -> 연결이 끊긴 또다른 새로운 시작점부터 이 과정을 계속 반복



n = int(input())
maps = [list(map(int, input())) for _ in range(n)] # 인접 행렬 방식
# print(maps)

# 방문처리용
visited = [[False]*n for _ in range(n)]


# 모든 정점을 확인해서 시작점이 될 수 있는지 확인. 시작점이 가능하면 dfs 탐색 GO
for i in range(n):
    for j in range(n):
        if visited[i][j] == False and maps[i][j] == 1:
            #print('(',i,',',j,')') #시작점 확인용 코드
            
            home_cnt = 0 #####
            dfs(i, j)
            ls.append(home_cnt)
            # cnt개수가 원래 0이였다가 dfs함수 호출 후 값이 집개수(한 단지 당)로 세팅돼 있을거임.



print(len(ls))
ls.sort()
for h in range(len(ls)):
    print(ls[h])
