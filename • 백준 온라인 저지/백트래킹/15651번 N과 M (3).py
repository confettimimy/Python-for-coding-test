# 같은 수를 여러 번 골라도 됨 + 순서 상관 있음 -> 중복 순열 
from itertools import product


# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
n, m = map(int, input().split()) # (ex) 1~3 중에서 1개를 고른 수열

ls=[]
for i in range(1, n+1):
    ls.append(i)

array = sorted(list(product(ls, repeat=m)))

for case in array:
    #print(case)
    for number in case:
        print(number, end=' ')
    print('')

