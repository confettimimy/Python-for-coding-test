from itertools import combinations

ls = ['OXOX', 'XOXO', 'XOOX', 'OXXX']
# 길이는 주어지는 변수마다 항상 다름

def solution(ls):
    
    re = [0]*len(ls)
    
    for num in range(1, len(ls)):
        for case in list(combinations(ls, num)):
            #print(case) # ex) ['OXOX', 'XOXO']
            
            for one in case:
                for i in range(len(one)):
                    if one[i] == 'O':
                        re[i] = 1
                        if re == [1]*len(ls):
                            return num # 최소값 리턴하고 메서드 종료 
            re = [0]*len(ls)#####

print(solution(ls))

'''
2. n가지의 보험 종류(여기선 4가지)가 주어졌을때
보험 갯수를 최소한 적게 하면서 모든 항목이 O가 될 수 있는
그 때의 보험 갯수 최소값을 구하여라.




동일한 보험 종류를 두 번 이상 뽑으면 안됨. permutations 불가
서로 다른 종류의 보험을 뽑아야 보험 갯수를 따질 수가 있음.


가장 바깥쪽의 for문을 돌리면서   ls에서 보험 뽑는 갯수를 1부터 시작.
1부터 시작하면서 맞는 조건에 걸리면 최소값을 출력해낼 수가 있음.


re = [0]*len(ls)#####
초기화 해주어야함!

'''
