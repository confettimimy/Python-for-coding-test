from itertools import permutations
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
operator_num = list(map(int, sys.stdin.readline().split()))
# 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수

oper = '' #복잡하니까 문자열로 만들기 
for i in range(len(operator_num)):
    if i==0:
        oper += '+' * operator_num[i]
    elif i==1:
        oper += '-' * operator_num[i]
    elif i==2:
        oper += '*' * operator_num[i]
    elif i==3:
        oper += '/' * operator_num[i]
#print(oper)
oper = list(oper)
for o in range(len(oper)):
    if oper[o]== '/':
        oper[o] = '//'
#print(oper)



# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.
# 또, 나눗셈은 정수 나눗셈으로 몫만 취한다.

# 주어진 연산자를 모두 사용하지 않고 모든 수의 사이에 연산자를 끼워넣을 수도 있다.
possible = set()
#maxx = 0
#minn = 0
for case in list(set(list(permutations(oper, len(a)-1 )))): # set을 이용한 중복제거를 통해 시간초과 문제 해결(동일한 요소가 있기 때문에 중복이 발생할 수 밖에 없다)
    #print(case)
    s = ''
    for i in range(len(a)-1): 
        s += str(a[i]) #숫자
        
        s = str(eval(s))
        #print(s,'s의 상태 ')
            
        s += case[i] #연산자
    s += str(a[-1])

    s = str(eval(s))  #앞에서부터 순차적으로 계산된 최종 결과값
    #print(s,'result')
    

    possible.add(int(s))
    '''if maxx < int(s):
        maxx = int(s)
    if minn > int(s):
        minn = int(s)'''


#print(maxx)
#print(minn)
possible = list(possible)
print(max(possible))
print(min(possible))


'''시간초과 문제해결
   list(set(list(permutations(oper, len(a)-1 ))))
   삼성 폴더에 있는 연산자끼워넣기 1 문제에서도 걸렸듯이 또 기억을 못했다.
   당시에도 set 중복제거를 통해 시간초과를 해결했다.
   위 코드를 통한 중복제거를 하면 꽤나 많은 연산, 루프 돌 필요가 없어짐을 확인할 수 있다.
   permutations에서 set() 중복제거를 이용한 가지치기=백트래킹 문제였다.(=필요없는 경우 연산x 쳐내기)
'''

'''문제풀이 후기
   '연산자끼워넣기' 원본 문제에서는 s 문자열 하나를 한번에 만든 다음, 계산을 앞에서부터 순차적으로 진행했지만
   이번에는 앞에서 식을 만들어감과 동시에 연산을 진행했다. 연산을 진행한 뒤 또 연산자-숫자 붙여서 또 계산하고 .. (또 붙이고)
   저번 풀이 방법과 이 정도의 차이..? 코드를 조금 더 효율적으로 사용하려는 노력을 했다.
'''
