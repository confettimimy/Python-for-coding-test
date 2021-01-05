import re

def solution(files):
    # 문자열을 숫자 기준으로 split
    # [사용예시] re.split(r"([0-9]+)", file)
    answer = [re.split( r"([0-9]+)" , file ) for file in files]
    
    answer = sorted(answer, key=lambda x: (x[0].upper(), int(x[1])) )
    # HEAD 부분을 기준으로 정렬 시, 문자열 비교 시 대소문자 구분을 하지 않는다.
    
    result = ["".join(one_file) for one_file in answer]
    
    return result

