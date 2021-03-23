import sys
sys.setrecursionlimit(10000)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    
    maps[x][y] = 0 # @

    #visited[x][y] = 1
    cnt = 0 # 모눈종이 한 지점에서의 공기 접촉 면의 개수

    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]

        if maps[nx][ny] ==1: #and visited[nx][ny] ==0:
            
            # 현 지점(nx, ny)의 사방면 탐색문
            for ch in range(4):
                cx = nx + dx[ch]
                cy = ny + dy[ch]
                if maps[cx][cy] == 0: # maps[nx][ny] 지점의 사방면을 탐색하며 0인 부분(공기)이라면
                    cnt += 1
                    if cnt >= 2: # 탐색시간단축, 굳이 4번 이상일 필요 없음. 2변 이상이기만 하면
                        #maps[nx][ny] == 0 #해당 지점 치즈 녹는다. 1 -> 0으로 변경하기. ---> dfs호출된 순간 해당 지점은 @ 부분에서 이미 0으로 바뀌니까 중복되지 않게 해야함.
                        dfs(nx, ny)
                        break # 현 지점(nx, ny)의 사방면 탐색문만 종료



n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]

#visited = [ [0]*m for _ in range(n) ]



answer = 0 # maps에서의 모든 치즈가 녹는 데 걸리는 시간

count = 0

for i in range(n):
    for j in range(m):
        
        if maps[i][j] == 1: #and visited[i][j] == 0:

            for che in range(4):
                ni = i + dx[che]
                nj = j + dy[che]
                if maps[ni][nj] == 0:
                    count += 1
                    if count >= 2: # 사면 중 두면 이상이 공기에 노출되어 '녹는 치즈'일 경우
                        dfs(i, j) # (i, j) 주변 사방면이 아닌, 현 지점이여야 함!
                        answer += 1 # dfs 한 번 실행될 때마다! ('c'인 부분 한번에 녹기)
                        break

print(answer)
