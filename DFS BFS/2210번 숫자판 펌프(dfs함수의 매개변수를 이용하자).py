
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, num):
    global possible
    if len(num) == 6:
        possible.add(num)
        return
    #num += str(board[x][y])
    
    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]

        if 0<=nx<5 and 0<=ny<5:
            dfs(nx, ny, num+str(board[nx][ny]))


board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

#visited = [[False]*5 for _ in range(5)]
#이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며,


possible = set()
#임의의 위치에서 시작
for i in range(5):
    for j in range(5):
        num=''
        dfs(i, j, str(board[i][j])) #이렇게 하니까 정답// dfs함수의 매개변수를 이용하자. <= 중요 포인트
        #possible.add(num) #이렇게 하면 하나만 넣어짐. 왜냐 이미 윗줄 dfs(i,j)에서는 여러번 실행되는데 이렇게 하면 마지막 하나만 되는셈

#print(possible)
print(len(possible))

