'''기존 인접행렬 방식에 인접 연결 조건에 대각선이 하나 추가된 문제'''
import sys
sys.setrecursionlimit(1000000)


# 상, 하, 좌, 우, 대각선
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

def dfs(x, y):
    visited[x][y] = True

    for p in range(8):
        nx = x + dx[p]
        ny = y + dy[p]

        # 여기서 m,n 바꿔고치니까 오류해결. 이전엔 여기가 문제여서 틀렸었을 것
        if 0 <= nx < m and 0 <= ny < n: ##########
            if maps[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)



m, n = map(int, input().split()) # 8 19

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

visited = [[False]*n for _ in range(m)]

count = 0 # 글자의 개수

for i in range(m):
    for j in range(n):
        # 여기 (i, j)는 모두 범위 내이기 때문에(이중포문), 범위 내 조건은 추가 안시켜도 됨
        if maps[i][j] == 1 and visited[i][j] == False:
            dfs(i, j) # dfs 뿌리 한 번 뻗으면 하나의 글자
            count += 1

print(count)
