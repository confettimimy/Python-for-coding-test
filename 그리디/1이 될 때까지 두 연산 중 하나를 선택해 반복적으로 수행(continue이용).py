n, k = map(int, input().split())

count = 0 #최소 횟수 구하기

# n이 1이 될 때까지
while n > 1: ###

  if n % k == 0: #n이 k로 나누어떨어질 때만 가능
    n /= k # 2연산 : n을 k로 나눈다
    count += 1
    continue # 1, 2 두 과정 중 하나를 반복적으로 선택하여 수행
             # 두 연산 모두 되지 않도록 continue를 이용해 아래코드를 실행되지 않도록 한다
  n -= 1 # 1연산 : n에서 1을 뺀다
  count +=1


print(count)
