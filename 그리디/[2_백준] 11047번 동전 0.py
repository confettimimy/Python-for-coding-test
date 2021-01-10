n, k = map(int, input().split())

count = 0 #필요한 동전 최소 개수
coin_types = []
for _ in range(n):
    coin_types.append(int(input()))

coin_types.sort(reverse = True)
#print(coin_types)

for coin in coin_types:
    if k >= coin:
        count += (k//coin)
        k = k % coin
        if k==0:
            break

print(count)
