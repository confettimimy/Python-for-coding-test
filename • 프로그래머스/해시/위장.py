def solution(clothes):
    dic = dict()
    for cloth in clothes: #초기화
        dic[cloth[1]] = 0
        
    for cloth in clothes:
        dic[cloth[1]] += 1
    print(dic)
    
    
    
    ls = list(dic.values())
    print(ls)
    
    answer = 1
    for num in ls:
        answer *= (num+1)
    return answer-1

'''
1. (headgear의 수 + 1) 1을 더 해주는 이유는 headgear를 착용하지 않을 수도 있기 때문입니다.
2. (eyewear의 수 + 1 ) 1을 더 해주는 이유는 eyewear를 착용하지 않을 수도 있기 때문입니다.
3. 두 수는 각각 독립적이기 때문에 1번 2번의 수를 곱하고 - 1 (모두 안입는 경우는 존재하지 않으므로)
'''
