import sys
sys.setrecursionlimit(10000)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    visited[x][y] = True

    for p in range(4):
        nx = x + dx[p]
        ny = y + dy[p]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False:
                if maps[nx][ny] == maps[x][y]: # 이전 색과 같을 경우
                    dfs(nx, ny)



n = int(input())

maps = [list(input()) for _ in range(n)]

#print(maps)



visited = [[False]*n for _ in range(n)]

cnt_1 = 0 # 일반인이 보는 영역의 개수
cnt_2 = 0 # 적록색맹인 사람이 보는 영역의 개수

colors = ['R', 'G', 'B']

# 정상인인 경우
for a in range(len(colors)):
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and maps[i][j] == colors[a]:
                dfs(i, j)
                cnt_1 += 1
                
visited = [[False]*n for _ in range(n)] # 다시 초기화해주어야함!! 앞을 실행하면 모두 True처리 돼있기 때문.

# 적록색맹인 경우
for i in range(n):
    for j in range(n):
        if maps[i][j] == 'R':
            maps[i][j] = 'G'
colors.remove('R')
#print(maps)

for b in range(len(colors)):
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and maps[i][j] == colors[b]:
                dfs(i,  j)
                cnt_2 += 1


print(cnt_1, cnt_2)

