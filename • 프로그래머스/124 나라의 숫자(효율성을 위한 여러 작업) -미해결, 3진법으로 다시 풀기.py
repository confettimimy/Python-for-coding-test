from itertools import product # 순열+중복가능
def solution(n):
    ls = '124'
    all_case = []
    count = 0 # 횟수 세기
    for num in range(1, 15):
        for case in product(ls, repeat=num):
            if count == n-1:
            #len(all_case) == n-1: # 효율성을 위해 일단 앞에것만 계산
                r = ''.join(case)
                '''r =''
                for one in case:
                    r += str(one)'''
                return r # break만으로는 하나의 루프밖에 빠져나올 수 없으니 메서드 종료 --> 이 처리가 중요했음!!! 
            count += 1
            #all_case.append(0) # all_case[n]값만 궁굼한거니까 이전값들은 일단 0으로 셋팅. 개수만 세기용
            # ---> 더 높은 효율성을 위해 ls에 append시키지 말고 count를 세자.
         
