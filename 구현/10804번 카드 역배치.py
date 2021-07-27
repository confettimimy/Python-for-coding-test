ls = [i for i in range(1, 21)]
#print(ls)

for _ in range(10):
    a, b = map(int, input().split())

    ls[a-1:b] = reversed(ls[a-1:b])
    #print(ls, '뒤집은 후 ')

for one in ls:
    print(one, end=' ')
