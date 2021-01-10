n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.extend(B) ### A = A.extend(B) 이런 식으로 쓰지말기!

A.sort()

for i in A:
    print(i, end=' ')

