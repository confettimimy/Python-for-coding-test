'''0, 1, 2 라는 조건이 반복되므로 '3으로 나누었을 때의 나머지'를 떠올릴 수 있어야 한다.'''

n = int(input())
ls = list(map(int, input().split()))

# 012012...
count = 0

for i in range(n):
    if ls[i] == count % 3:
        count += 1

print(count)
        
