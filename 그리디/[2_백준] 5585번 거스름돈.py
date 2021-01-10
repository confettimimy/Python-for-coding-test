n = int(input())
leave = 1000 - n #거스름돈

count = 0
coin_types = [500, 100, 50, 10, 5, 1]

for coin in coin_types:
    if leave >= coin:
        count += (leave//coin)
        leave = leave % coin
        if leave == 0:
            break
print(count)
