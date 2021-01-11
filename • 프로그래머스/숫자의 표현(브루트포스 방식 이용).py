def solution(n):
    
    sum = 0
    count = 0 # 표현하는 방법의 개수
    
    for i in range(1, n+1): # 브루트포스 방식으로 시작점으로 가능한지 조회
        #여기를 간과해 틀렸었음. ex) 1부터 시작해서 15까지 해야함.
        
        while sum <= n: # 15일때까지만 해보면 됨
            if sum == n:
                count += 1
                break
                
            sum += i
            i += 1
            #print(i, end=' ') #확인용
        #print()
            
        # while문 빠져나오면 초기화
        sum = 0
        
    
    return count

