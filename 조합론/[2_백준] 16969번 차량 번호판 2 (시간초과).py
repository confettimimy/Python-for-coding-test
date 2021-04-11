from itertools import combinations
import sys
import time

start_time = time.time() 

'''
cc 문자문자
cd 문자숫자
dd 숫자숫자'''

usable_num = [i for i in range(10)]
usable_char = [chr(c) for c in range(97, 122+1)] 


input_type = sys.stdin.readline()


result = 1
tmp = ''
# 메모제이션 기법 해봐도 시간이 줄어들지 않음. 
re_memo1 = 0
re_memo2 = 0
for c in input_type:
    
    if c == 'c':
        if tmp != '' and tmp[-1] != 'c': # 이전이 중복된 문자가 아니라면
            re_memo = len(list(combinations(usable_char, 1))) # -> len(usable_char)으로만 해도됨.
            result *= re_memo
            tmp += c
        elif tmp == '': # 처음 c라면
            result *= len(list(combinations(usable_char, 1)))
            tmp += c    
        else: # 이전과 중복돼 'cc'라면
            result *= (len(list(combinations(usable_char, 1))) - 1)
            tmp += c


    if c == 'd':
        if tmp != '' and tmp[-1] != 'd': # 이전이 중복된 문자가 아니라면
            result *= len(list(combinations(usable_num, 1)))
            tmp += c
        elif tmp == '': # 처음 d라면
            result *= len(list(combinations(usable_num, 1)))
            tmp += c    
        else: # 이전과 중복돼 'dd'라면
            result *= (len(list(combinations(usable_num, 1))) - 1)
            tmp += c


print(result)
    
end_time = time.time()
print('time: ', end_time-start_time) # 시간초과문제 -> input_type을 길게 받을수록 실행시간이 길어짐.
