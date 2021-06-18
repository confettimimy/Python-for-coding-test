t = int(input()) # 189

a = 300
b = 60
c = 10

count = [0, 0, 0]

while True:
    if t == 0:
        break

    if t < c:
        break

    

    while t >= a:
        t-=a
        count[0] += 1

    while t >= b:
        t-=b
        count[1] += 1

    while t >= c:
        t-=c
        count[2] += 1


if t != 0:
    print(-1)
else: # t==0 이면
    for i in count:
        print(i, end=' ')
