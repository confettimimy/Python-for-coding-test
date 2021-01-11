import sys
sys.setrecursionlimit(100000)

def fibo(num):
    if num == 1 or num == 2:
        return 1
    elif num == 0:
        return 0
    return fibo(num-1) + fibo(num-2)


n = int(input())

print(fibo(n))


'''계속 런타임에러(RecursionError)와 메모리 초과 나오다가 
   n이 0일 때를 처리해주니까 끝내 맞게 나옴.'''
