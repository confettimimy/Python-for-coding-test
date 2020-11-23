import math

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

print(is_prime_number(4)) # 4는 소수가 아님
print(is_prime_number(7)) # 7은 소수임


'''특정한 자연수x가 소수인지 확인하기 위하여 바로 가운데 약수까지만 나누어떨어지는지 확인하면 된다.
   이 소수 판별 알고리즘에서 보이는 바와 같이, 제곱근까지만 확인해도 된다는 점에서 시간 복잡도를 매우 많이 개선할 수 있다.'''