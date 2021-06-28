from itertools import combinations
from itertools import permutations


n = int(input())
weight = list(map(int, input().split()))
# 100 2 1 3 100

possible = [] #가능한 모을 수 있는 에너지 양
energy = 0



#weight -> 아래 for문 안에서는 for_finding_max로 통한다

for for_finding_max in list(permutations(weight, len(weight))):
    
    for_finding_max = list(for_finding_max)
    
    '''tmp_weight = list(for_finding_max) #깊은복사 
    tmp_weight.remove( for_finding_max[0] )
    tmp_weight.remove( for_finding_max[-1] )'''


    print('------------for_finding_max :',for_finding_max)
    print(for_finding_max[1:len(for_finding_max)-1],'z')
    #왜 여기에 다시 안들지...? -> 아래 combinations부분에서 n을 사용해서 계속 []에서 1개 뽑는거였음 -출력으로 확인 
    energy = 0 #초기화
    for case in list(combinations(for_finding_max[1:len(for_finding_max)-1], 1)): 
        print(case)
        x = for_finding_max.index(int(case[0])) #인덱스값
        print(x,'인덱스 ')
        #print(for_finding_max) 

        energy += for_finding_max[x-1]*for_finding_max[x+1]
        print('에너지', energy)
        removed = for_finding_max[x]
        del for_finding_max[x] #인덱스 아웃 에러나니까 에너지값 구한후 값제거

        n -= 1
        print(for_finding_max,'end')
        for_finding_max.insert(x, removed)
        

    if energy not in possible:
        possible.append(energy) #하나의 에너지양 케이스 추가 



print(possible)
print(max(possible))
