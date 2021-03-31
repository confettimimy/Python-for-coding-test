import sys
sys.setrecursionlimit(1000000)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):

    visited[x][y] = True

    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]

        if 0 <= nx < n and 0 <= ny < n:
            if area[nx][ny] > rain_length:
                if visited[nx][ny] == False:
                    dfs(nx, ny)


n = int(input())

area = []
for _ in range(n):
    area.append(list(map(int, input().split())))

visited = [[False]*n for _ in range(n)]


safety = 0 # 안전영역의 개수

max_num = 0
tmp = []
for k in range(n):
    tmp.append(max(area[k]))
max_num = max(tmp)

ls = []
for rain_length in range(max_num): # '비의 양에 따른 모든 경우를 다 조사'

    for i in range(n):
        for j in range(n):
            if area[i][j] > rain_length and visited[i][j] == False:
                dfs(i, j)
                safety += 1 # dfs가 한번 실행될 때마다 안전영역개수 +1 / 길이는 상관없음
                
    ls.append(safety)
    safety = 0

    visited = [[False]*n for _ in range(n)] # 다음에 영향가지 않도록 다시 셋팅(이 처리를 안해줘서 계속 0으로 나왔었음)


#print(ls)
print(max(ls))
