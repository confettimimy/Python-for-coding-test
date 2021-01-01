# (평균을 구하는 문제가 아닙니다)
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

c = int(input())

average = 0
number = 0

for _ in range(c):
    ls = list(map(int, input().split()))

    average = (sum(ls)-ls[0]) / ls[0]

    for i in range(1, len(ls)+1):
        if ls[i] > average:
            number += 1

    print( number )
           #/(len(ls)-1) )
    #print( format( , ".3f")) 
