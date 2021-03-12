'''시간초과 문제
--> 2차원 배열의 합을 구하는 절차는 누적합을 이용하므로 누적합을 매번 계산할 필요 없이 한번 계산한 결과는 저장해놓있다가 필요할 때 꺼내 쓰면 된다.'''

import sys

n, m = map(int, sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

#print(arr)



sum = 0
k = int(sys.stdin.readline())
for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().split())
    
    # 위를 인덱스화용으로 처리
    i-=1
    j-=1
    x-=1
    y-=1

    tmp = j

    while True:
        if i==x and j==y:
            sum += arr[i][j]
            break

        if j==y:
            sum += arr[i][j]
            i+=1
            j=tmp  

        sum += arr[i][j]
        if j==y:
            break
        j += 1



    print(sum)
    sum = 0 # 초기화

    
