import sys
sys.setrecursionlimit(1000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(a, b):
    visited[a][b] = True

    for p in range(4): # 현재 위치에서 네 방향 확인
        nx = x + dx[p]
        ny = y + dy[p]

        if 0 <= nx < m and 0 <= ny < n: #  X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)
            if maps[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)



answer = 0 # 필요한 흰 지렁이 수

t = int(input())
for _ in range(t): # 테스트 케이스 수
    m, n, k = map(int, input().split())

    maps = [[0]*m for _ in range(n)]
    print(maps)
    for _ in range(k):
        x, y = map(int, input().split())
        maps[x][y] = 1
    print(maps)
    
    visited = [[False]*m for _ in range(n)]


    for i in range(n):
        for j in range(m):
            
            dfs(i, j)
            answer += 1
            
    print(answer) # 각 테스트 케이스 수마다 필요한 흰 지렁이의 개수 출력
