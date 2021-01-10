n, m = map(int, input().split())

count = 0
result = []

ls1 = [input() for _ in range(n)]
ls2 = [input() for _ in range(m)]


result = set(ls2) - (set(ls2)-set(ls1))

result = sorted(list(result))


print(len(result))
for answer in result:
    print(answer)

