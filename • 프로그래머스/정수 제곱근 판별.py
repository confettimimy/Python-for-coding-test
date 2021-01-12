import math

def solution(n):
    
    for x in range(1, int(math.sqrt(n))+1):
        if x**2 == n:
            print(x)
            return (x+1)**2
    
    # for문을 다 돌았는데도 if문에 걸리지 않으면
    return -1

