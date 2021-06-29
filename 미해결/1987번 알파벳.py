import sys
sys.setrecursionlimit(1000000)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):

    global answer

    visited[x][y] = True
    
    #알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
    if board[x][y] not in answer:
        answer += board[x][y]

    print(answer)
    

    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]

        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] not in answer:# 이동한 지점 알파벳이 history 이력에 없다면
                if visited[nx][ny] == False:
                    dfs(nx, ny)


                    
r, c = map(int, input().split())

board = []
for _ in range(r):
    board.append( input() )
print('board :', board)

visited = [[False]*c for _ in range(r)]


history = []
answer = '' # dfs 한 번 실행시 갈 수 있는 길이


dfs(0, 0)



print(answer)
