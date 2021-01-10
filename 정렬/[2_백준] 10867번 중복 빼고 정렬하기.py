n = int(input())

ls = list(map(int, input().split()))

answer = sorted(set(ls))

for i in answer:
    print(i, end=' ')
