from itertools import permutations
import sys

k = int(sys.stdin.readline())
a = sys.stdin.readline().split()

num_list = [i for i in range(0, 10)]

possible = set()
first = False
actual_min=0
for case in list(permutations(num_list, k+1)):
    status = False
    # case = (0, 2, 1)
    s = ''
    for j in range(k):
        if len(s)%2 != 0: #홀수이면 2<3과 같이 계산할 수 있는 형태
            if eval(s) == False:
                status = True # 해당 케이스는 시간낭비 하지 말고 바로 패스
                continue # 해당 케이스는 시간낭비 하지 말고 바로 패스
        s += str(case[j])
        s += a[j]
    s += str(case[-1])

    if status == False:

        if eval(s) == True:
            result = ''
            for c in s:
                if c.isdigit():
                    result += c
            if first==False:
                actual_min = result #맨처음으로 add되는 값은 어차피 최대값, 시간초과 해결을 위해 최댓값 min(possible)계산을 줄여주자.
                first=True
            possible.add(int(result))



#print(possible)
possible = list(possible)

print(max(possible))

# 21(X), 021(O) : 최솟값 앞이 0이면 int시 지워지므로 0이 달린 원본값으로 다시 만들어줘야함
min_result = '' 
short = len(str(actual_min))
if short != (k+1): 
    min_result = '0'*((k+1)-short)  +  str(actual_min)
    print(min_result)
else:
    print(actual_min)


'''시간초과 해결하기
+) min값과 max값을 구할 때는 >>어차피 순차적으로 조합을 구하기 때문에<< min값은 맨처음 통과한 값으로, max_value는 계속 값을 넣어주면서 구하면 쉽게 구할 수 있다!
'''

