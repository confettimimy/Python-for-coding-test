from itertools import permutations
def solution(expression): # "100-200*300-500+20"
    ls=[]
    tmp=''
    for c in expression: #숫자와 연산자 구분해서 ls에 넣기 -중요### 전에 이부분에서 항상 걸림.
        if c.isdigit():
            tmp+=c
        else:
            ls.append(tmp)
            tmp=''
            ls.append(c)#연산자 넣기
    ls.append(tmp) #마지막숫자의 처리
    print(ls)
    
    operator = set()
    for c in expression:
        if c in ('+', '-', '*'):
            operator.add(c)
    operator = list(operator)
    
    for case in permutations(operator, len(operator)): #큰 틀
        print(case)
        # ('-', '+', '*')
        new = []
        for oper in range(len(case)): # '-'인것 일단 첫번째로 다 돌면서 다 처리해버리기, 그 다음 '+'.... =우선순위 높은 계산부터 처리
            
            for i in range(1, len(ls)-1):
                if ls[i] == case[oper]:
                    temp = eval(ls[i-1] + ls[i] + ls[i+1])
                    print(temp)
                    #new.append(ls[:i-1])
                    for a in ls[:i-1]:
                        new.append(a)
                    new.append(temp)
                    #new.append(ls[i+1+1:])
                    for b in ls[i+1+1:]:
                        new.append(b)
                    print(new)
