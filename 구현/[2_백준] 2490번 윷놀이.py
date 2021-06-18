
for _ in range(3):
    ls = list(map(int, input().split()))

    d = ls.count(1) #등
    b = ls.count(0) #배


    if b==1 and d==3:
        print('A') #도
    elif b==2 and d==2:
        print('B') #개
    elif b==3 and d==1:
        print('C') #걸
    elif b==4:
        print('D') #윷
    elif d==4:
        print('E') #모
