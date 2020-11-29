# 전역변수 개념 다시보기(  )


# 방향배열 ('대각선상에 집이 있는 경우는 연결된 것이 아니다'라는 문제조건 때문에 상하좌우만)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ls = [] # 각 단지에 속하는 집의 수
home_cnt = 0 #####

def dfs(x, y):
    visited[x][y] = True
    global home_cnt #####
    home_cnt += 1
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and maps[nx][ny] == 1:
            dfs(nx, ny)



n = int(input())
maps = [list(map(int, input())) for _ in range(n)] # 인접 행렬 방식
# print(maps)

# 방문처리용
visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False and maps[i][j] == 1:
            #print('(',i,',',j,')') #시작점 확인용 코드
            
            home_cnt = 0 #####
            dfs(i, j)
            ls.append(home_cnt)



print(len(ls))
ls.sort()
for h in range(len(ls)):
    print(ls[h])
