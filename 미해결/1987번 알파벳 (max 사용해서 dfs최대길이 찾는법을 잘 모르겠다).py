'''나는 계속 한 길로만 감.
그렇게 가도 맞긴 한건데, '최대'길이는 아님.
한 길로만 쭉 가고. 그 외의 가능성도 탐색해야하는데
max(ans, cnt)비교하며 최대일때 실행하는 걸로 가야하는데 그게 안됨 지
'''
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):

    global ans, cnt
    cnt += 1
    ans = max(ans, cnt)

    global visited, history
    visited[x][y] = True
    history += board[x][y]
    
    for a in range(4):
        print(a,'z')
        nx = x + dx[a]
        ny = y + dy[a]

        if 0<=nx<r and 0<=ny<c:
            if visited[nx][ny] == False:
                #새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
                if board[nx][ny] not in history:
                    visited[nx][ny] = True
                    dfs(nx, ny)
                    visited[nx][ny] = False



r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(input())

visited = [[False]*c for _ in range(r)]

ans = 0 #최종
cnt = 0 #말이 지날 수 있는 최대의 칸 수
history = ''
dfs(0, 0)

for case in visited: #그냥 확인용 
    print(case)

print(history)
print(ans)
