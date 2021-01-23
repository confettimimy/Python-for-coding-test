'''board = [[0,0,0,0,0],
            [0,0,1,0,3],
            [0,2,5,0,1],
            [4,2,4,4,2],
            [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]'''

def solution(board, moves):
    stack = []
    lose_doll_count = 0

    
    for pick_location in moves: # ex) 1, 5...
        
        for i in range(len(board)):
            if board[i][pick_location-1] > 0: # 세로줄 기준으로 해야함!
                stack.append(board[i][pick_location-1])
                '''board[i][pick_location-1] 이 부분을 계속 board[i][0]이라 써서 틀렸었음.'''
                board[i][pick_location-1] = 0 # 뽑힌 인형 자리는 0으로 처리해주어야함
                
                # 방금 넣은 값이 이전 값과 같다면
                if len(stack) >=2 and stack[-2] == stack[-1]:
                    stack.pop()
                    stack.pop()
                    lose_doll_count += 2
                break # 0이 아닌 값을 한 번 만나면 그 다음을 실행하지 않고 다음 move 배열 요소로 넘어간다. = 루프 하나만 나온다
                

    return lose_doll_count


print( solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]) )
