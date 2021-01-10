# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라.
n = 1260
count = 0

# 가장 큰 단위의 화폐부터 차례대로 확인하기
coin_types = [500, 100, 50, 10]


for i in range(len(coin_types)):
  count += n // coin_types[i] #몫은 동전 개수에 더하기
  n = n % coin_types[i] #n을 몫과 동전수 곱한 값을 뺀 값으로 다시 세팅

print('동전의 최소 개수: ', count)
