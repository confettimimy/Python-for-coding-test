n, m = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(input())


color = ['W', 'B']
tmp = []
status = chess[0][0]
count = 0 #지민이가 다시 칠해야 하는 정사각형 개수
before = chess[0][0] #각 행의 제일 앞 요소 기록해두기
for i in range(n):
    
    for j in range(m):
        print(status)
        if chess[i][j] == status:
            tmp = list(color) #color원본값 바뀌지않게 복사해서 tmp로 사용하기
            tmp.remove(status)
            status = tmp[0]
        else:
            count+=1
            
            # 상태는 계속 번갈아갈수 있게 바꿔주기
            tmp = list(color) #color원본값 바뀌지않게 복사해서 tmp로 사용하기
            tmp.remove(status)
            status = tmp[0]
            
    # 한줄이 끝나면 status값 다시 세팅해야함
    # 바로 앞 행의 가장 맨 처음요소랑 다르게 설정
    tmp2 = list(color)
    tmp2.remove(before)
    status = tmp2[0]
    
    before = chess[i][0]####여기가 맞는것 같은데...(   )

print(count)
            
