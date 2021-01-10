n = int(input())

ls = []
for _ in range(n):
    ls.append(int(input()))

ls.sort()

for x in ls:
    print(x)
