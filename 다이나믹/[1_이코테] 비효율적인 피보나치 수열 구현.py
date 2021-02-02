# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

# 하지만 피보나치 수열을 이렇게 구현하면 심각한 문제가 생길 수 있다.
# f(n)함수에서 n이 커지면 커질수록 수행시간이 기하급수적으로 늘어나기 때문