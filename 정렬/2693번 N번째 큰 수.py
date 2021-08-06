N = 3

t = int(input())
for _ in range(t):
    ls = list(map(int, input().split()))

    ls.sort(reverse=True)

    print(ls[N-1])
