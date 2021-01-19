from collections import Counter

def solution(s):
    
    count = 0 # 이진 변환의 횟수
    discarded_0_count = 0 # 제거된 모든 0의 개수
    
    while True:
        if s == "1":
            break

        # 1. x의 모든 0을 제거합니다.
        print(Counter(s))
        discarded_0_count += s.count('0')
        num =  Counter(s)['1']
        s = "1" * num
        
        # 2. x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
        c = len(s) # 0 제거 후 길이
        s = format(c, 'b')
        # https://docs.python.org/ko/3/library/functions.html#bin 참고
        
        count += 1

        
    return [count, discarded_0_count]



print( solution("110010101001") )
