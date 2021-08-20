import sys
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0] # 틀렸던 이유: dx dy가 (-1,0)이면 당연히 기존 x축이동 관념대로 왼쪽으로 간다고 착각했음. 여기서 nx는 열이다! 세로! 시선을 바꿔 생각해야 했다. 앞으로 dfs응용을 위해 이런 디테일도 기억하자
dy = [0, 0, -1, 1]
def dfs(x, y):
    visited[x][y] = True


    if pan[x][y]=='-':

        for a in range(2, 4): #양옆으로만 감
            nx = x + dx[a]
            ny = y + dy[a]

            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==False:
                    if pan[nx][ny] == '-':
                        dfs(nx, ny)
                        
    elif pan[x][y]=='|':

        for a in range(2): #양옆으로만 감
            nx = x + dx[a]
            ny = y + dy[a]

            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==False:
                    if pan[nx][ny] == '|':
                        dfs(nx, ny)

                        


n, m = map(int, input().split())
pan = []
for _ in range(n):
    pan.append(input())

'''
-||-
-|--
--|-
-|--
'''

visited = [[False]*m for _ in range(n)]

count = 0
for i in range(n):
    for j in range(m):
        if pan[i][j] == '-' or '|':
            if visited[i][j]==False: # +범위내 있는지 확인 조건처리는 여기선 안해도됨 
                dfs(i, j)
                count += 1

print(count)
