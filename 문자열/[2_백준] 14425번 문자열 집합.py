n, m = map(int, input().split())

S = set() #총 N개의 문자열로 이루어진 집합 S
for _ in range(n):
    S.add(input())

count = 0
for _ in range(m):
    s = input()
    if s in S:
        count += 1
print(count)
