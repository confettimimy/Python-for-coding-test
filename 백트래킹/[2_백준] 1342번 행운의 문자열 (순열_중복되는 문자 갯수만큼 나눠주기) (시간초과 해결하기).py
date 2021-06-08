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
from collections import Counter
import math


s = input()



answer = set() # 비어있는 집합을 만들기 위해서는 다음과 같이 사용한다.
string = ""
count = 0

for case in list(permutations(s, len(s))):
    string = "".join(case)
    chk = False #초기화 

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            chk = True
            break
        
    # for문 다 돌며(= 한 케이스의 문자열) 확인 다 함
    if chk == False: # 여전히 False라면
        #answer.add(string) # 중복제거를 위해 집합 자료형 사용
        # @ -> 시간초과 문제를 해결하기 위해 갯수만 세자 (어차피 개수 세는 것이 목적인 문제니까)
        count += 1


#print(answer)
#print(len(answer)) # @



'''왜 메모리 초과가 나는가에 대한 고민'''
# @
# 행문의 문자열이 '어떻게 생겼는지' 볼 필요는 없으니, 시간절약을 위해 갯수 위주로만 계산하는 방식으로 문제를 해결
counter = dict(Counter(s))

for a in counter.values():
    count //= math.factorial(a) # math.factorial(x)


print(count)

# 중복값 만큼 나눠주었는데 이번엔 시간초과 문제가 뜸




'''
<중복 순열 처리를 해준다>
이를 위해 입력받은 문자열에서 중복되는 문자의 갯수를 센다.
그 갯수만큼 팩토리얼하여 (위에서 구한 result 값에 해당하는) 행운의 문자열 갯수에다 나눠주어야 하기 때문이다.

ex. "aabbbaa"의 경우, a는 4번, b는 3번 중복된다.
따라서 result[0]의 값 / 4!*3! 을 해주어야 한다. 중복된 행운의 문자열을 제거하기 위해서다.
'''
