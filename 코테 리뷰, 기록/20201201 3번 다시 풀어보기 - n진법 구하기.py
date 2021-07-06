'''
0 1 2 3 4 5
10 11 12 13 14 15
20 21 22

중복뽑기가능 순서중요
중복순열 product
'''
from itertools import product

'''
# 6진법 구하기
ls = [i for i in range(6)]
answer = []

for num in range(1, 6+1):
    
    for case in list(product(ls, repeat=num)):
        re = ''
        for one in case:
            re += str(one)
        re = int(re)
        
        if re not in answer:
            answer.append(re)


print(answer[15])'''


#--------------------------------------------------


n = 5
t=15

# N진법 구하기
ls = [i for i in range(n)]
answer = []

for num in range(1, n+1):
    
    for case in list(product(ls, repeat=num)):
        re = ''
        for one in case:
            re += str(one)
        re = int(re)
        
        if re not in answer:
            if len(answer) == t:
                break
            answer.append(re)


print(answer[-1])
