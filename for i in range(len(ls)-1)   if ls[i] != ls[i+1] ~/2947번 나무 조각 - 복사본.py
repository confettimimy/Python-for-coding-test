objective = [i for i in range(1, 6)]

ls = list(map(int, input().split()))

i=0
while True:
    if ls == objective:
        break
    if i == 4:
        i = 0

    tmp = 0
    if ls[i] > ls[i+1]:
        tmp = ls[i] #둘의 위치를 서로 바꾼다.
        ls[i] = ls[i+1]
        ls[i+1] = tmp
        
        for p in ls: #바꿀때마다 출력
            print(p, end=' ')
        print()
        
    i+=1
