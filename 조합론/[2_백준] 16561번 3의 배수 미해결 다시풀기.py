'''
nPr = nCr X r! 
nCr = n! / (n-r)!r!

'''

#from itertools import permutations
import math


n = int(input()) # 3의 배수 12

# 이를 3의 배수 자연수 3개로 분리하는 경우의 개수 구하기
# () + () + () = n

n //= 3 # 4

#ls = [o for o in range(1, n)] # [1, 2, 3]




if n <= 4: # (3 ≤ n ≤ 3000)
    # 예외처리 ValueError: factorial() not defined for negative values
    if n==3:
        print(1)
    elif n==4:
        print(3)
else: 
    # 순열 (n-1)P3
    print(  math.factorial(n-1) // math.factorial(n-1-3)  )


'''시간 제한 0.1초기 때문에 굳이 permutations 라이브러리까지 사용하며 +코드 비효율적으로까지 구하지 말자'''
