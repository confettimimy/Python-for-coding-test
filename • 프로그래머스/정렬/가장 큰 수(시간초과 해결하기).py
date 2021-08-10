from itertools import permutations

def solution(numbers):
    #시간초과를 해결하기 위한 작업
    #numbers리스트에서 맨 앞자리수가 가장 큰 순서대로 정렬하기!
    numbers2 = list(map(str,numbers)) # ['6','10','2']
    
    for i in range(len(numbers2)):
        if len(numbers2[i])==1:
            numbers2[i]+='00'  # 아래 정렬시 x[0]기준으로 정렬한다음 x[1]기준으로 정렬할때 index out 초과에러가 나지 않도록 하기 위한 작업
    
    numbers2.sort(key=lambda x:(x[0], x[1]), reverse=True)
    print(numbers2)
    
    for j in range(len(numbers2)):
        if numbers2[j][1:]=='00':
            numbers2[j] = numbers2[j][0] 
    print(numbers2)
    
    return "".join(numbers2)
    
    
    
    '''<시간초과> 처음했던 비효율적인 코드 -> 모든경우 탐색
    ls = []
    for case in permutations(numbers, len(numbers)):
        #print(case)
        
        num=''
        for a in case:
            num += str(a)
        ls.append(int(num))
    
    ls.sort(reverse=True)
    return str(ls[0])
    '''
