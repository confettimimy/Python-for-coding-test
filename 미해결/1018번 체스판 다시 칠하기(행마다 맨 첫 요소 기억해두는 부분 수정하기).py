n, m = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(input())


color = ['W', 'B']
tmp = []

status1 = 'B'
status2 = 'W'

before1 = chess[0][0] #각 행의 제일 앞 요소 기록해두기
before2 = chess[0][0]

correct1 = ['B', 'W'] # BWBWBWBW... 이렇게 시작할때의 경우
correct2 = ['W', 'B'] # WBWBWBWB... 이러한 패턴으로 갈 경우

count1 = 0 #지민이가 다시 칠해야 하는 정사각형 개수
count2 = 0
 


for i in range(n):
    
    for j in range(m):
        print(status1)
        if chess[i][j] == status1:
            tmp = list(color) #color원본값 바뀌지않게 복사해서 tmp로 사용하기
            tmp.remove(status1)
            status1 = tmp[0]
        else:
            count1 += 1
            
            # 상태는 계속 번갈아갈수 있게 바꿔주기
            tmp = list(color) #color원본값 바뀌지않게 복사해서 tmp로 사용하기
            tmp.remove(status1)
            status1 = tmp[0]
    print()
            
    # 한줄이 끝나면 status값 다시 세팅해야함
    # 바로 앞 행의 가장 맨 처음요소랑 다르게 설정
    if i%2 == 0:
        before1 = correct1[0] #틀렸던 이유: 이를 뒤 세줄코드 뒤에놔서..여기다가 놔야하는데
    else:
        before1 = correct1[1]
    
    tmp = list(color)
    tmp.remove(before1)
    status1 = tmp[0]



for i in range(n):
    
    for j in range(m):
        print(status2,'z')
        if chess[i][j] == status2:
            tmp = list(color) #color원본값 바뀌지않게 복사해서 tmp로 사용하기
            tmp.remove(status2)
            status2 = tmp[0]
        else:
            count2 += 1
            
            # 상태는 계속 번갈아갈수 있게 바꿔주기
            tmp = list(color) #color원본값 바뀌지않게 복사해서 tmp로 사용하기
            tmp.remove(status2)
            status2 = tmp[0]
    print()
            
    # 한줄이 끝나면 status값 다시 세팅해야함
    # 바로 앞 행의 가장 맨 처음요소랑 다르게 설정
    if i%2 == 0:
        before2 = correct2[0] #틀렸던 이유: 이를 뒤 세줄코드 뒤에놔서..여기다가 놔야하는데
    else:
        before2 = correct2[1]
    
    tmp = list(color)
    tmp.remove(before2)
    status2 = tmp[0]


print(count1, count2)
print(min(count1, count2))
            
