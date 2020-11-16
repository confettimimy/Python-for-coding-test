def solution(s):
    
    s_list=[] #(문자열) 정렬라이브러리를 사용하기 위해 리스트 자료형을 이용
    upper = [] #대문자들을 담아둘 임시 리스트
    
    for c in s:
        if c.isupper() == True: #대문자이면
            upper.append(c)
        else:
            s_list.append(c)
    
    s_list.sort(reverse=True)
    upper.sort(reverse=True)
    
    s_list.extend(upper)
    # 현재는 리스트 형태 -> 문자열 형태로 바꾸기
    result=''
    result = ''.join(s_list) #"".join(리스트) 혹은 "특정문자열".join(리스트) 형태
    # print(result) # 확인
    
    return result

