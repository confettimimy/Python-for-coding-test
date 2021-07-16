scores = []
for _ in range(10):
    scores.append(int(input()))


case = []
sum=0
for i in range(len(scores)):
    sum += scores[i]
    case.append(sum)
#print(case)


diff = []
for k in range(len(case)):
    diff.append( abs(100-case[k]) )
#print(diff)



#만약 100에 가까운 수가 2개라면 (예: 98, 102) 마리오는 큰 값을 선택한다.
idx = []
if diff.count( min(diff) ) >= 2: #diff에 동일한 최솟값이 두 개 이상 있다면
    for a in range(len(diff)):
        if diff[a] == min(diff):
            idx.append( a )
    gg = []
    #print(idx,'idx')
    for b in range(len(idx)):
        gg.append(case[  idx[b] ]) ##조심하기!
    #print(gg)
    print( max(gg) )
else:
    print( case[diff.index(min(diff))] )
