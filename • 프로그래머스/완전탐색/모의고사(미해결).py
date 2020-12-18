def solution(answers):
    counts = [0, 0, 0]
    
    ls1 = [1, 2, 3, 4, 5]
    ls2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ls3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for a in answers:
        if a == ls1[a%5]:
            counts[0] += 1
        if a == ls2[a%8]:
            counts[1] += 1
        if a == ls3[a%10]:
            counts[2] += 1
    print(counts)
    
    counts.sort(reverse = True)
    
    
    '''
    dic = {}
    dic[1] = counts[0] # 요소 추가
    dic[2] = counts[1]
    dic[2] = counts[2]
    
    dic.sort(key=lambda x: x[1]) # 맞은 개수 count순으로 정렬
    
    return list(dic.keys())'''
    
