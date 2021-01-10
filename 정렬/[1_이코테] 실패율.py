def solution(N, stages):

    answer = []
    length = len(stages)
    
    for i in range(1, N+1):

        # 해당 스테이지에 머물러 있는 사람 수 계산
        count = stages.count(i)
        
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        answer.append( (i, fail) )
        
        length -= count

        
    
    answer.sort(key=lambda t: t[1], reverse = True)
    
    answer = [a[0] for a in answer]
    
    return answer

