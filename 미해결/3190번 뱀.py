n = int(input())
k = int(input())

board = [[0]*n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1 #해당 위치에 사과가 위치
for case in board:
    print(case)

l = int(input())
dummy = []
for _ in range(l):
    ls = input().split()
    x = int(ls[0]) #x초 뒤에
    c = ls[1] # 방향 l, d
    dummy.append((x, c))
#dummy = [(3, D), (15, L), (17, D)]

snake = [(0, 0)]
end = False
save = 0
for minute in range(1, 60): #뱀은 매 초마다 이동

    for i in range(len(dummy)):
        
        if dummy[i][0] == minute:
            
            # D 오른쪽으로 이동
            if dummy[i][1] == 'D':
                #먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
                snake.append( (snake[-1][0]+1, snake[-1][1]) )
                if board[snake[-1][0]+1][snake[-1][1]] == 1: #이동한 칸에 사과가 있다면
                    board[snake[-1][0]+1][snake[-1][1]] = 0
                    #뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
                    if snake[-1] in dummy:
                        end = True
                        save = minute
                        break
                    if not (0<= snake[-1][0] <n and 0<= snake[-1][1] <n):
                        end = True
                        save = minute
                        break
                else: #이동한 칸에 사과가 없다면
                    del snake[0]#꼬리치우기
            # L 왼쪽으로 이동
            elif dummy[i][1] == 'L':
                snake.append( (snake[-1][0]-1, snake[-1][1]) )
                if board[snake[-1][0]-1][snake[-1][1]] == 1: #이동한 칸에 사과가 있다면
                    board[snake[-1][0]-1][snake[-1][1]] = 0
                    #뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
                    if snake[-1] in dummy:
                        end = True
                        save = minute
                        break
                    if not (0<= snake[-1][0] <n and 0<= snake[-1][1] <n):
                        end = True
                        save = minute
                        break
                else: #이동한 칸에 사과가 없다면
                    del snake[0]#꼬리치우기
    if end==True:
        break
    
print(board)
print(snake)
print(save)
