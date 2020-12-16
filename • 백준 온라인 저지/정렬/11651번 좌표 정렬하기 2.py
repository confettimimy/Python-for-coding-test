import sys

n = int(input())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] ###

#print(arr)

arr.sort(key=lambda x: (x[1], x[0]) )

#print(arr)

for ls in arr:
    print(ls[0], ls[1])
