'''
모든 경우의 수를 나열해보기
거기서 조건(인접 문자들이 모두 달라야함)에 들어맞는 경우의 개수를 세서 출력시킨다.
'''


'''
순서가 중요한가? O
중복 뽑기 가능한가? X
-> 순열(중복순열X)
'''

from itertools import permutations

s = input()


string = ""
count = 0
for case in list(permutations(s, len(s))):
    string = "".join(case)
    chk = False #초기화 

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            chk = True
            continue ### 여길 바꿔야함 
    # for문 다 돌며(= 한 케이스의 문자열) 확인 다 함
    if chk == False: #여전히 False라면
        count += 1 #인접 문자 모두 다 다른 경우임




print(count)


# 과정 흐름 다시 파악하고 고치기!
