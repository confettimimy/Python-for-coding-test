import math

m = int(input())
n = int(input())


perfect_square_number = [] # 완전제곱수인 수를 담을 리스트

for i in range(m, n+1):
    if math.sqrt(i) - int(math.sqrt(i)) == 0:
        perfect_square_number.append(i)

if len(perfect_square_number) == 0:
    print(-1)
else:
    print(sum(perfect_square_number))
    print(min(perfect_square_number))

    
