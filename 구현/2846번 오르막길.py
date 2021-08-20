n = int(input())
p = list(map(int, input().split()))


before = p[0]
sum = 0
possible = []

for i in range(1, n):
    if p[i] > before: #오르막길
        sum += (p[i]-before)
        #print(sum)
    else:
        if sum!=0:
            possible.append(sum)
        sum = 0
        
    if sum!=0: #이부분을 처리안해줘서 틀림. 마지막부분이 계속 오르막길이면 append안된 채로 있음. else문에 안걸리기 때문에
        possible.append(sum)
        
    before = p[i]


#print(possible)

if len(possible)==0:
    print(0)
else:
    print(max(possible))
