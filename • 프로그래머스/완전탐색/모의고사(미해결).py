def solution(answers):
    counts = [0, 0, 0]
    
    ls1 = [1, 2, 3, 4, 5]
    ls2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ls3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(0, len(answers)):
        if answers[i] == ls1[i%5]:
            counts[0] += 1
        if answers[i] == ls1[i%8]:
            counts[1] += 1
        if answers[i] == ls1[i%10]:
            counts[2] += 1
    print(counts,'z') #여기서 일단 무언가가 잘못됨..
    
    final = [[1], [2], [3]]
    for k in range(3):
        final[k].append( counts[k] )
    
    final.sort(key=lambda x: x[1], reverse = True)
    
    print(final)
    print(final[0][0])

    # 딕셔너리 자료형은 리스트와 다르게 sort() 어트리부트를 갖고있지 않는다
