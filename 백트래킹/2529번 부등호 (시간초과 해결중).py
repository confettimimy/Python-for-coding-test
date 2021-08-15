from itertools import permutations
import sys

k = int(sys.stdin.readline())
a = sys.stdin.readline().split()

num_list = [i for i in range(0, 10)]


actual_min = '' # 실질 최소값
actual_max = 0 # 실질 최대값
first = False
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
            if first==False:
                actual_min = result
                first = True
            if actual_max < int(result): #기존보다 큰 값 생길때마다 계속 업데이트시켜주기
                actual_max = int(result)



print(actual_max)
print(actual_min)



'''시간초과 해결하기
[접근1]  min값과 max값을 구할 때는 >>어차피 순차적으로 조합을 구하기 때문에<< min값은 맨처음 통과한 값으로, max_value는 계속 값을 넣어주면서 구하면 쉽게 구할 수 있다!
         => 이 방식을 이용해 코드를 고쳤더니 여전히 시간초과 문제가 발생한다.
         => 파이썬 자체가 겁나 느려서 그런 것 같다. .  파이썬 쓰는 것이 갑자기 현타오기 시작했다.
         
[접근2]  permutations를 쓰면 부등호를 고려하지 않고 모든 경우를 다 구하므로 메모리 초과가 발생합니다.
         부등호를 고려하여 (앞뒤 크기를 고려하여) 조합을 만들어야 합니다.
         dfs방법으로 푸는 것을 추천합니다.
  
'''

