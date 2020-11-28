import sys
sys.setrecursionlimit(10000) #재귀깊이설정

# 상하좌우 + 대각선
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def dfs(x, y):
    visited[x][y] == True # map에서 현재 위치 방문처리

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i] # (nx, ny)는 이동 후 위치

        # (1) 이동한 위치가 맵을 벗어나지 않는 유효한 범위인지 확인
        # (2) 이동한 위치가 한번도 방문된 적 없는 곳인지 확인
        # (3) 이동한 위치가 이동가능한 곳인지 확인
        if (0 <= nx < w and 0 <= ny < h) and (visited[nx][ny] == False) and (maps[nx][ny] == 1):
            dfs(nx, ny)



while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    # 2x2행렬의 인접행렬 방식
    maps = []
    for _ in range(h):
        maps.append(list(map(int, sys.stdin.readline().split())))

    # 방문처리용
    visited = [[False]*w for _ in range(h)]
    print(visited)

    count = 0
    # 이제 2x2행렬 map의 모든 지점을 돌며 시작점으로 가능한 곳을 찾자.
    # 시작점으로 가능하면 dfs 수행 go
    for m in range(h):
        for n in range(w):
            if visited[m][n] == False and maps[m][n] == 1: # 아직 방문처리가 안되어있고 그 지점이 섬이라
                dfs(m, n)
                count += 1

    print(count)


    
