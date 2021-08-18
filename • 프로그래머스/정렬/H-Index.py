def solution(citations):
    citations.sort(reverse=True) # [6 5 3 1 0]
    h_index = citations[0]+1 #6
    
    for _ in range(citations[0]+1):
        h_index-=1
        #print(h_index,'h_index')
        
        cnt=0
        copy = list(citations)
        for i in range(len(citations)):
            if citations[i] >= h_index:
                cnt+=1
                copy.remove(citations[i])
        #print(cnt)
        #print(copy)
        if not cnt >= h_index:
            continue #해당 h_index 케이스는 아닌거임.
            
        #나머지 논문이 모두 h번 이하 인용됨이 확인되면 그게 정답
        status = True
        for one in copy:
            if not one <= h_index:
                status = False # 해당 케이스 h_index는 실패
                break
        if status==True: #여전히 True라면
            return h_index #그게 정답 
        
        
