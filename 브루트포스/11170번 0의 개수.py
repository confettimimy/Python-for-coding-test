t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    ls = [i for i in range(n, m+1)]
    #print(ls)

    count = 0
    for num in ls:
        for c in str(num):
            if c == '0':
                count+=1

    print(count)
