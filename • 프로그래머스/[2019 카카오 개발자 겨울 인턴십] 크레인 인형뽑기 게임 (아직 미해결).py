# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    stack = []
    lose_doll_count = 0
    
    for doll_location in moves:
        k = 0
        for i in board[doll_location-1]:
            if i == 0:
                k += 1 # 몇 번째인지 세기 용
            if i != 0: # 0이 아닌 순간
                stack.append(i) # 바구니에 넣고
                
                if len(stack) >= 2 and i == stack[-2]: # 그 이전 요소와 같다면
                    stack.pop()
                    stack.pop()
                    lose_doll_count += 2
                
                board[doll_location-1][k] = 0 # 다음에 또 뽑히지 않게 인형이 원래 있던 위치를 비워준다.
                # board의 원본을 바꿔주었어야 함
                break
                
    print(stack)
    
    print(lose_doll_count)
