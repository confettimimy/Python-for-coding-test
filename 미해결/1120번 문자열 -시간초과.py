from itertools import product #중복순열 
import sys
ls = sys.stdin.readline().split()
A = ls[0]
B = ls[1]


'''
이제 A의 길이가 B의 길이와 같아질 때 까지 다음과 같은 연산을 할 수 있다.

1. A의 앞에 아무 알파벳이나 추가한다.
2. A의 뒤에 아무 알파벳이나 추가한다.
'''
oper = [1, 2] #연산 선택지
answer_min = 0
per_list = list(set(product(oper, repeat = len(B)-len(A)))) #len(B)-len(A)는 연산을 해야하는 횟수
#print(per_list)

first = False
for case in per_list:
    A_new = A #변형된 A를 담을 A_new
    for cal in case:
        if cal == 1:
            A_new = '*' + A_new
        elif cal == 2:
            A_new += '*'
    #print(A_new, B)


    count = 0
    # A와 B의 차이 계산하기
    for i in range(len(B)):
        if A_new[i] != B[i] and A_new[i] != '*':  # A요소가 '*'라면 같은걸로 침. 아무 알파벳이나 넣으라고 했으니 최소를 만들려면 그렇게 해야함
            count += 1

    if first==False:
        answer_min = count
        first = True

    if count < answer_min:
        answer_min = count


print(answer_min)
