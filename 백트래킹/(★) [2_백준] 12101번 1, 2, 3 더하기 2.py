from itertools import product

n, k = map(int, input().split())

# 정수n을 1,2,3의 합으로 구성

ls = [1, 2, 3]
good = []

#순서 중요, 중복 가능 = 중복순열 product
for i in range(1, n+1):
    for case in list(product(ls, repeat=i)):
        #print(case)
        if sum(case) == n:
            good.append(case)
            

if len(good)==0:
    print(-1)
else:
    if k <= len(good): #예제4 반례처리 
        answer = list(map(str, sorted(good)[k-1]))
        print("+".join(answer))
    else:
        print(-1) #예제4 반례처리 
            
