from collections import Counter
from copy import deepcopy #이차원배열의 깊은 복사!

def R(A):
    for i in range(len(A)):
        dic = dict(Counter(A[i]))
        arr = []
        #각각의 수가 몇 번 나왔는지 알아야 한다. 
        for num in dic.keys():
            if num!=0 and dic[num]!=0:
               arr.append( (num, dic[num]) )
        # arr = (1, 1), (2, 1), (3, 1)
        #print(arr,'arr')
        
        
        # 그 다음, 수의 등장 횟수가 커지는 순으로,
        # 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다.
        arr.sort(key=lambda x:(x[1], x[0]))
        #print(arr,'arr 정렬후')
        
        A[i] = [] # 바뀐 결과줄로 A배열 원본 바꾸기
        for two in arr:
            A[i].append(two[0])
            A[i].append(two[1])

    #print(A,'R함수 수행후')
    #print(deepcopy(A), '깊은복사 ') 
    return deepcopy(A) #들여쓰기 잘하자!!!!


# 크기가 가장 큰 행은 2번 행이고, 나머지 행의 뒤에 0을 붙여야 한다.
def add_0(A):   
    max_w = 0 #가장 큰 행의 갯수 
    for a in A:
        if len(a) > max_w:
            max_w = len(a)
    add_num = 0
    for a in A:
        if len(a) != max_w:
            add_num = max_w - len(a)
            for _ in range(add_num):
                a.append(0)
    return deepcopy(A)






r, c, k = map(int, input().split())
A = []
for _ in range(3):
    A.append(list(map(int, input().split())))
#print(A, '처음 A배열 원본모습')




minute = 0

# 3. 다음에 적용되는 연산은 행의 개수 < 열의 개수이기 때문에 C 연산이다.
first = False
while True:
    if 0<=r < len(A) and 0<=c < len(A[0]) and A[r][c] == k:
        break
    if minute > 100:
        break

    if first == False: # 가장 처음에는 행의 개수 ≥ 열의 개수 이기 때문에, R 연산이 적용된다.
        A = R(A)
        A = add_0(A)
        #minute += 1
        first = True
        print(A, 'R연산 수행후')
        continue

    #행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
    if len(A) > 100:
        A = A[:101]
    if len(A[0]) > 100:
        for h in range(len(A)):
            A[h] = A[:101]
            
        
    
    # R연산인지, C연산인지 판별한다.
    if len(A) >= len(A[0]): # R 연산
        A = R(A)
        #A = add_0(A)
        minute += 1
        print(A, 'R연산 수행후')
    else: # C 연산
        #여기에 c연산 구현 -> 여기가 잘못됐다. -> 계속해서 손보는중
        max_temp_length = 0
        status = False
        for yul in range(len(A[0])): # 세로 한 줄
            
            tmp = []
            for i in range(len(A)):
                tmp.append(A[i][yul])

            dic2 = dict(Counter(tmp)) 
            arr2 = []
            for number in dic2.keys():
                if number!=0 and dic2[number]!=0: #수를 정렬할 때 0은 무시해야 한다.
                    arr2.append( (number, dic2[number]) )

            arr2.sort(key=lambda x:(x[1], x[0]))

            temp = []
            for tw in arr2:
                temp.append(tw[0])
                temp.append(tw[1])
            #print(temp,'temp')
            if len(temp) > max_temp_length:
                max_temp_length = len(temp)
            #print(max_temp_length) #6


            if status == False:
                new = [[0]*len(A[0]) for _ in range(max_temp_length)] #계속 초기화되면 다 0으로 셋팅되니까 1번만 실행시키도록 하기
                status = True

            for o in range(max_temp_length): # 0~5
                if o <= len(temp)-1:
                    new[o][yul] = temp[o]


        # 모든 열 실행후 도출된 결과 new 이차원배열 
        A = deepcopy(new)
        print(A,'A의 모습 확인해보자')

                
        #A = add_0(A)
        minute += 1
        #print(A,'C연산 수행후')

        

if minute > 100:
    print(-1)
else:
    print(minute)





'''<중요 point>
2차원 이상의 다차원 리스트는 리스트를 완전히 복사하려면 copy 메서드 대신 copy 모듈의 deepcopy 함수를 사용해야 합니다.

C연산을 잘못 구현해놔서 다시 고치느라 애를 먹었다
'''


'''<오류 참고>
[[1, 2, 1], [2, 1, 3], [3, 3, 3]] 처음 A배열 원본모습
[[2, 1, 1, 2, 0, 0], [1, 1, 2, 1, 3, 1], [3, 3, 0, 0, 0, 0]] R연산 수행후
0
[1, 1, 2, 1, 3, 1] temp
1
[3, 1, 1, 2] temp
2
[1, 1, 2, 1] temp
3
[1, 1, 2, 1] temp
4
[3, 1] temp
5
[1, 1] temp
[[1, 3, 1, 1, 3, 1], [1, 1, 1, 1, 1, 1], [2, 1, 2, 2, 0, 0]] C연산 수행후
2
'''
