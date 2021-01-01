n = int(input())

count = 0 # 총 자릿수

for i in range(1, n+1):
    count += len(str(i))

print(count)
