def solution(n):
    y = [] # 약수들을 넣을 리스트
    
    for i in range(1, n+1):
        if n % i == 0:
            y.append(i)
    
    return sum(y)
