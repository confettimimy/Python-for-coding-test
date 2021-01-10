# (평균을 구하는 문제가 아닙니다)
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

c = int(input())

average = 0
number = 0

for _ in range(c):
    ls = list(map(int, input().split()))

    average = (sum(ls)-ls[0]) / ls[0]

    for i in range(len(ls)):
        if i == 0:
            continue
        if ls[i] > average:
            number += 1
            
    print( format( number/ls[0]*100 , ".3f")+'%') # 문자열 연결 시 ','를 이용하면 한칸이 띄워지는데 '+'를 이용하면 바로 딱 붙는다.
    
    number = 0 # 다음 행 계산을 위해 초기화 꼭 잊지말기 (자주 실수하는 부분)

