def solution(n):
    n = str(n) #문자열 자료형으로 바꾼 뒤
    
    s_list=[]
    for i in n: #하나씩 꺼내며
        s_list.append(i) #리스트에 넣는다
    
    #이제 리스트 자료형이 되었으니 정렬 라이브러리 사용이 가능하다.
    s_list.sort(reverse = True) #원본을 바꾼다.

    return int(''.join(s_list))


# [더 효율적인 방식]

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

