import sys
sys.setrecursionlimit(1000000)


size = 0 # global 변수로 선언 (dfs메서드 내에서도 통용되게)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    global size
    '''전역변수를 지역 범위 안에서 사용하고 싶다면 지역 영역에서 global 키워드를 사용한다. 이렇게 하면 지역 범위 안에서 전역변수를 사용할 수 있게 된다.'''
    size += 1
    
    visited[x][y] = True

    for p in range(4):
        nx = x + dx[p]
        ny = y + dy[p]

        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)
    
    

n, m, k = map(int, input().split())


matrix = [[0]*m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    r -=1
    c -=1

    matrix[r][c] = 1 # 음식물 떨어진 곳

#print(matrix) # 확인

visited = [[False]*m for _ in range(n)]

size_ls = []

for i in range(n):
    for j in range(m):

        if matrix[i][j] == 1 and visited[i][j] == False:
            size = 0
            dfs(i, j)
            size_ls.append(size)

            
print(max(size_ls))
#print(size_ls, '확인용')
