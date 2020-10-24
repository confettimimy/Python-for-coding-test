from itertools import permutations 

def solution(numbers):
    
    case = list(permutations(numbers, len(numbers))) #순열 - 일렬로 나열
    #print(case)
    
    #case.sort(reverse = True)
    #print(case[0])
    
    s=''
    s_list=[]
    for i in range(len(case)): #튜플 하나당
        for j in range(len(case[i])): #튜플 원소 개수당
            s += str(case[i][j])
        s_list.append(s)
        s='' #이걸 꼭 해주어야 함
            

    #print(s_list) #확인
    
    # 현재 s_list는 문자열 상태이니 숫자로 바꿔 정렬시키자
    for s in s_list:
        s = int(s)
    
    s_list.sort(reverse=True) #큰 수 순으로 정렬

    return s_list[0]
