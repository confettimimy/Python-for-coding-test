from itertools import permutations


A, B = input().split()
C = 0

possible = set()

for case in list(permutations(A, len(A))):
    #print(case)
    case = "".join(case) #'0001'


    #C는 0으로 시작하면 안 된다. ('0', '0', '0', '1')
    if len(str(int(case))) == len(case):  # 0으로 시작하지 않는 경우만 '0001' ###여기가 문제였는데 이렇게 처리하면됨.
        if int(case) < int(B):
            possible.add(int(case))



if len(possible)==0:
    print(-1)
else:
    print(max(list(possible)))
