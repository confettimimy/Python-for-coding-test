import math
import itertools
import sys

n, m = map(int, sys.stdin.readline().split())
sure = list(map(int, sys.stdin.readline().split())) # 3 4



ls = [i for i in range(0, 10)]
ls = list( set(ls) - set(sure) )
#print(ls)



# 0~9, 총 10개
result = set()
if n==m:
    print(math.factorial(m))
else:
    #n개 중 m개는 무조건 들어감
    #n-m개는 ls에서 골라야함
    for case in list(itertools.combinations(ls, n-m)):
        re = list(sure)
        for i in case:
            re.append(i)
        #print(list(itertools.permutations(re, n))) -> 예외: 77
        # 7은 무조건 들어가면서 중복순열 가능
        for case in list(itertools.product(re, repeat = n)):
            status = False
            for s in sure:
                if s not in case: #sure에 있는 문자가 하나라도 없다면 
                    status = True
            if status == False: #여전히 False라면
                #print(case)
                result.add(case)

   
    print(len(list(result)))

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
'''시간초과 문제 발생
dfs나 순열조합을 이용한 백트래킹 방식으로 풀면 시간초과가 발생한다.
주어진 n과 m을 이용해서 수학적으로 풀 수 있다.
'''
