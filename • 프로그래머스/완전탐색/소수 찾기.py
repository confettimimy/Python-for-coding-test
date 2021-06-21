from itertools import permutations
import math

def solution(numbers):
    answer = []
    true_answer = [] #2차검증 후 최종답 
    numbers = list(numbers)
    
    for i in range(1, len(numbers)+1):
        for case in list(permutations(numbers, i)):
            answer.append( int("".join(case)) )
    answer = list(set(answer))
    
    print(answer,'중간점검')
    
    # 이제 소수인지를 판별해야함!
    for one in answer:
        chk = True
        for j in range(2, int(math.sqrt(one))+1):
            if one%j==0:
                chk=False
                break
                
        if chk == True: #여전히 True라면 = for문 다 돌면서 나누어 떨어지는 것이 하나도 없었다면
            true_answer.append(one)
            
    if 0 in true_answer:
        true_answer.remove(0)
    if 1 in true_answer:
        true_answer.remove(1)

    print(true_answer)
    return len(true_answer)
            
