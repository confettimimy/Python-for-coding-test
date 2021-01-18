def solution(n):
    
    i = n+1
    while True: # 조건 1
        if str(bin(i)).count('1') == str(bin(n)).count('1'): # 조건 2
            return i # 조건 3
        i += 1
        
