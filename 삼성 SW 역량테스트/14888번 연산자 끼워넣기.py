from itertools import permutations
import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
operater = list(map(int, sys.stdin.readline().split())) #차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
oper = ''
for i in range(4):
    if i==0:
        oper += ('+' * operater[i])
    elif i==1:
        oper += ('-' * operater[i])
    elif i==2:
        oper += ('*' * operater[i])
    elif i==3:
        oper += ('/' * operater[i])
oper = list(oper)
# 연산자의 위치가 각각 어디냐에 따라 달라진다.


possible = set()
for case in list(set(list(permutations(oper, len(oper))))): # @@@
    #print(case)
    answer = str(A[0]) 
    tmp = list(A)[1:] #A와 case의 인덱스 맞춰주기
    for k in range(len(case)):
        #A[k] case[k]
        answer += case[k]
        answer += str(tmp[k]) # '3+4'   '*5'
        #print(answer,'문자열 상태 ')


        # 나눗셈은 정수 나눗셈으로 몫만 취한다.
        mid = []
        if '/' in answer:
            mid = answer.split('/')
            mid = list(map(int, mid))
            if mid[0] < 0 and mid[1] > 0: # 음수를 양수로 나눌 때는, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
                answer = str(( (mid[0]*(-1))//mid[1] )*(-1))
            else:
                answer = str( mid[0]//mid[1] ) #문자열로 계속 일관되게 맞춰주기 
        else: #일반적인 경우 
            answer = str(eval(answer))

            
        # 아래 문자열로 접근하는 것이 왜 안되냐면, 한자리수만 들어오는 것이 아니라 10 11까지 피연산자로 들어올 수 있기 때문에
        # answer[-2]로 접근하면 안된다는 것이다. 혹여나 answer[-1]이 한자리수가 아니라 두자리수 11이였다면? answer[-2]가
        # 내 예상대로의 +같은 연산자가 아니라 숫자로 잡힌다는 말이다.
        '''if answer[-2]=='/':
            if int(answer[:-3+1]) < 0 or int(answer[-1]) > 0: ###아 두자리.....
                print(int(answer[:-3+1]),'ㅇㅇㅇㅇㅇㅇㅇ', int(answer[-1])) #뭔가 잘못됨 . . . 
                # 음수를 양수로 나눌 때는, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
                answer = str(-(-int(answer[:-3+1]) // int(answer[-1]) ))
            else:
                # 나눗셈은 정수 나눗셈으로 몫만 취한다.
                answer = str( int(answer[:-3+1]) // int(answer[-1]) )
        else: # 일반적인 경우  
            answer = str(int(eval(answer))) # 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.'''
           

    possible.add(answer)


possible = list(map(int, possible))
#print(possible)
print(max(possible))
print(min(possible))


'''예제3 겨우 맞추었더니 시간초과 문제
순열조합을 이용한 브루트포스 문제....계속 시간초과 문제가 걸린다. . .
dfs말고 순열조합 모듈을 이용해서 시간이 느려지는 건 아닌 것 같다. <--순열조합 모듈 이용해도됨.
순열 조합 라이브러리를 그대로 써도되긴 한데.
항상 시간초과 문제가 걸림!
'부분수열의 합' 문제에서는 정렬 사용해서 처음부터 탐색하며 빨리 찾으면 break하는 방식으로 시간초과 문제해결.
이번에는 어떻게 해결할 것인지..?
'''


'''시간초과 문제 최종 해결 방법
set()으로 중복 제거를 했다.
PyPy3로 제출하든 Python3로 제출하든 상관없다.
위 @@@ 부분에서 중복제거 처리를 해주니 시간이 확연하게 줄어들었다.
순열같은 경우, 같은 종류의 요소가 여러개이면 중복이 다량 발생할 수도 있다. 예를들어 abc를 순열 돌리는거랑 aab를 순열 돌리는거랑 후자가 중복이 발생할 수 있다는 얘기
list(set(list(permutations(oper, len(oper)))))
다음과 같이 순열 라이브러리를 통한 결과 목록 중, 중복제거를 또 처리해줘서 시간초과 문제를 해결한 것은 이번이 처음이다.
이런 케이스도 있음을 잘 알아두자.

결론은, 직관적으로 풀기 위해 순열조합 라이브러리를 이용하는 것은 전혀 문제없다. dfs든 순열조합이든 방법일 뿐이다.
'부분수열의 합'문제나 이번 문제와 같이 가지치기를 잘해서 시간을 줄이면 된다.
'''
