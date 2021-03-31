import sys
sys.setrecursionlimit(10000000)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):

    global size
    size += 1

    visited[x][y] = True

    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]

        if 0 <= nx < n and 0 <= ny < m:
            if paper[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)


n, m = map(int, input().split())

paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

visited = [[False]*m for _ in range(n)]

size = 0


ls = [] # 각 그림마다의 size를 담을 리스트
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and visited[i][j] == False:
            dfs(i, j)
            ls.append(size)

            size = 0

print(len(ls))

if len(ls) == 0: # 아래와 같은 사항으로 예외처리해주기
    ls.append(0)
    
print(max(ls))


# 런타임에러
'''[예외]
1 1
0

위와 같이 그림이 없을 경우 다음과 같은 예외 상황이 있음.
    print(max(ls))
ValueError: max() arg is an empty sequence

'''
