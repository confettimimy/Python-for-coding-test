from itertools import permutations
import sys

k = int(sys.stdin.readline())
a = sys.stdin.readline().split()

num_list = [i for i in range(0, 10)]


actual_min=0
actual_max=0
per_list = list(permutations(num_list, k+1))
for case in per_list: #작은수부터 순서대로 조합 시작
    print(case, 'case')
    status = False
    # case = (0, 2, 1)
    s = ''
    for j in range(k):
        s += str(case[j])

        #여기 중간에 왔어야함!
        #if len(s)%2 != 0 and len(s)!=1: #홀수이면 2<3과 같이 계산할 수 있는 형태
        if len(s)!=1 and eval(s) == False:
            print('안되는경우 ')
            status = True # 해당 케이스는 시간낭비 하지 말고 바로 패스
            break # 해당 케이스는 시간낭비 하지 말고 바로 패스
        
        s += a[j]
        
    s += str(case[-1])

    if status == False and eval(s) == True:
        
        result = ''
        for c in s:
            if c.isdigit():
                result += c
        actual_min = result
        break # break하면 최종 for루프 바로 나와지는거 확인완료, 여기에 걸려있는 for문이 최종 for루프 밖에 없으니까 
        #@@@ 맨 처음 충족값 찾자마자 최종 for루프 break. 시간절약을 위해 중간과정은 다 빼고 맨앞부터 제일 첫번째, 맨뒤부터 제일 마지막꺼만 찾으면 됨.


per_list = list(reversed(per_list)) #정렬 대신
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
[접근1]  min값과 max값을 구할 때는 >>어차피 순차적으로 조합을 구하기 때문에<< min값은 맨처음 통과한 값으로, max_value는 계속 값을 넣어주면서 구하면 쉽게 구할 수 있다!
         => 이 방식을 이용해 코드를 고쳤더니 여전히 시간초과 문제가 발생한다.
         => 파이썬 자체가 겁나 느려서 그런 것 같다. .  파이썬 쓰는 것이 갑자기 현타오기 시작했다.
         
[접근2]  permutations를 쓰면 부등호를 고려하지 않고 모든 경우를 다 구하므로 메모리 초과가 발생합니다.
         부등호를 고려하여 (앞뒤 크기를 고려하여) 조합을 만들어야 합니다.
         dfs방법으로 푸는 것을 추천합니다.

         0 1 경우가 안되면 뒤에도 아예 안되는거니 0 1로 시작되는 뒷부분 모두를 배제해야하는데
         계속 계산을 하고있으니. . .  permutations을 쓰면 시간초과가 날 수밖에 없다.
         dfs를 이용해보는 방식 밖에.
  
'''

