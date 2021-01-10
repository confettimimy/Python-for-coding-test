# 같은 수를 여러 번 골라도 됨 + 순서 상관 있음 -> 중복 + 순열 
from itertools import product # 중복순열


# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
n, m = map(int, input().split()) # (ex) 1~3 중에서 1개를 고른 수열

ls=[]
for i in range(1, n+1):
    ls.append(i)

array = sorted(list(product(ls, repeat=m))) # 사전 순으로 증가하는 순서로 출력해야 한다

for case in array:
    
    for number in case:
        print(number, end=' ')
    print('')

'''
1 1 
1 2 
1 3 
1 4 
2 1 
2 2 
2 3 
2 4 
3 1 
3 2 
3 3 
3 4 
4 1 
4 2 
4 3 
4 4 
'''
