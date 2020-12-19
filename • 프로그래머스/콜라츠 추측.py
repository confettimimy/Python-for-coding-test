def solution(num):
    
    count = 0
    loop_cnt = 0
    while True:
        loop_cnt += 1
        if loop_cnt >= 500:
            return -1
        
        if num == 1:
            break
        
        if num % 2 == 0:
            num //= 2
        else:
            num = num*3 + 1
        count += 1
    
    return count

