def solution(x):
    answer = True
    
    p = 0
    for i in str(x):
        p += int(i)
    
    if x % p != 0:
        answer = False
    
    return answer
