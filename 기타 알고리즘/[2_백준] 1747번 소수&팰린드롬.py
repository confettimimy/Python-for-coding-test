import math


n = input()

# 소수 판별 함수
def is_prime_number(x):

    ### 1은 소수가 아님. 2,3은 소수가 맞음. 이 부분에 대한 예외처리를 안해줘서 99%에서 계속 걸렸었다
    if x == 1:
        return False

    
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임


while True:
    n = str(n) # n부터 시작
    
    # 팰린드롬 수인지 확인
    if "".join(list(n)) == "".join(list(reversed(list(n)))):
        # 소수인지 확인 
        if is_prime_number(int(n))==True:
            print(n)
            break

    n = int(n)
    n += 1
