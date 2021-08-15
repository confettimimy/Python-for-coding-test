from itertools import permutations
import sys

k = int(sys.stdin.readline())
a = sys.stdin.readline().split()

num_list = [i for i in range(0, 10)]


actual_min=0
actual_max=0
per_list = list(permutations(num_list, k+1))
for case in per_list: #작은수부터 순서대로 조합 시작
    status = False
    # case = (0, 2, 1)
    s = ''
    for j in range(k):
        if len(s)%2 != 0: #홀수이면 2<3과 같이 계산할 수 있는 형태
            if eval(s) == False:
                status = True # 해당 케이스는 시간낭비 하지 말고 바로 패스
                break # 해당 케이스는 시간낭비 하지 말고 바로 패스
        s += str(case[j])
        s += a[j]
    s += str(case[-1])

    if status == False:

        if eval(s) == True:
            result = ''
            for c in s:
                if c.isdigit():
                    result += c
            actual_min = result
            break # break하면 최종 for루프 바로 나와지는거 확인완료, 여기에 걸려있는 for문이 최종 for루프 밖에 없으니까 
            #@@@ 맨 처음 충족값 찾자마자 최종 for루프 break. 시간절약을 위해 중간과정은 다 빼고 맨앞부터 제일 첫번째, 맨뒤부터 제일 마지막꺼만 찾으면 됨.

per_list = sorted(per_list, reverse=True)
for case in per_list: #큰수부터 순서대로 조합 시작
    status = False
    
    s = ''
    for j in range(k):
        if len(s)%2 != 0: #홀수이면 2<3과 같이 계산할 수 있는 형태
            if eval(s) == False:
                status = True # 해당 케이스는 시간낭비 하지 말고 바로 패스
                break # 해당 케이스는 시간낭비 하지 말고 바로 패스
        s += str(case[j])
        s += a[j]
    s += str(case[-1])

    if status == False:

        if eval(s) == True:
            result = ''
            for c in s:
                if c.isdigit():
                    result += c
            actual_max = result
            break
            #@@@ 맨 처음 충족값 찾자마자 최종 for루프 break.
        

print(actual_max)
print(actual_min)



'''시간초과 해결하기
+) min값과 max값을 구할 때는 >>어차피 순차적으로 조합을 구하기 때문에<< min값은 맨처음 통과한 값으로, max_value는 계속 값을 넣어주면서 구하면 쉽게 구할 수 있다!
'''

