import sys
sys.setrecursionlimit(1000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):

    global sheep, attacker

    visited[x][y] = True

    if maps[x][y] == 'o':
        sheep += 1
    elif maps[x][y] == 'v':
        attacker += 1

    
    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]

        if 0 <= nx < r and 0 <= ny < c:
            if maps[nx][ny] != '#':
                if visited[nx][ny] == False:
                    dfs(nx, ny)
            



r, c = map(int, input().split())

maps = []
for _ in range(r):
    maps.append(input())

visited = [[False]*c for _ in range(r)]

answer_sheep = 0
answer_attacker = 0

for i in range(r):
    for j in range(c):

        if maps[i][j] != '#':
            if visited[i][j] == False:
                
                sheep = 0
                attacker = 0
                
                dfs(i, j)

                if sheep>attacker:
                    answer_sheep += sheep
                else:
                    answer_attacker += attacker


print(answer_sheep, answer_attacker)
