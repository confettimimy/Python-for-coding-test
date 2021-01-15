import sys
sys.setrecursionlimit(1000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True

    for p in range(4): # 현재 위치에서 네 방향 확인
        nx = x + dx[p]
        ny = y + dy[p]

        if 0 <= nx < n and 0 <= ny < m: #  X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1) ### (n, m 주의)
            if maps[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)



t = int(input())
for _ in range(t): # 테스트 케이스 수
    answer = 0 # 필요한 흰 지렁이 수
    
    m, n, k = map(int, sys.stdin.readline().split())

    maps = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split()) # input을 sys.stdin.readline로 치환하여 쓰면 시간이 260ms나 단축됨
        maps[b][a] = 1 ####### 이렇게 해야 배추가 있는 위치 그래로의 모양대로 나옴
    '''for q in maps: # 확인용
        print(q)'''
    
    visited = [[False]*m for _ in range(n)]


    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1 and visited[i][j] == False:
                dfs(i, j)
                answer += 1
            
    print(answer) # 각 테스트 케이스 수마다 필요한 흰 지렁이의 개수 출력
