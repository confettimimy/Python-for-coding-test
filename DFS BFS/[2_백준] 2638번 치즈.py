dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):

    visited[x][y] = 1
    cnt = 0 # 모눈종이 한 지점에서의 공기 접촉 면의 개수

    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]

        if maps[nx][ny] ==1 and visited[nx][ny] ==0:
            
            # 현 지점(nx, ny)의 사방면 탐색문
            for ch in range(4):
                cx = nx + dx[ch]
                cy = ny + dy[ch]
                if maps[cx][cy] == 0: # maps[nx][ny] 지점의 사방면을 탐색하며 0인 부분(공기)이라면
                    cnt += 1
                    if cnt >= 2: # 탐색시간단축, 굳이 4번 이상일 필요 없음. 2변 이상이기만 하면
                        maps[nx][ny] == 0 #해당 지점 치즈 녹는다. 1 -> 0으로 변경하기.
                        break # 현 지점(nx, ny)의 사방면 탐색문만 종료


n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]

visited = [ [0]*m for _ in range(n) ]


for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
