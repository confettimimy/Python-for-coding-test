from collections import Counter
def solution(s):
    #print(type(s)) #집합 자료형이 아닌 문자열임을 확인.
    s = s[2:-2]
    ls = s.split('},{')
    #print(ls)
    new = []
    for a in ls:
        new.append( list(map(int, a.split(','))) )
    #print(new,'z')
    
    ls2 = []
    for i in new:
        for j in i:
            ls2.append(j)
    dic = dict(Counter(ls2))
    #print(dic)
    
    ls3 = [] # 딕셔너리 등장횟수순으로 정렬을 하기 위한 작업
    for num in dic.keys():
        ls3.append([num, dic[num]])
    #print(ls3)
    ls3.sort(reverse=True, key=lambda x:x[1])
    #print(ls3)
    
    # 정답출력
    result = []
    for one in ls3:
        result.append(one[0])
    return result
    
