t = int(input())

arr = [list(map(int, input().split(','))) for _ in range(t)]

for a in arr:
    print(a[0] + a[1])

