'''chr(): 아스키코드를 문자열로 변환하는 함수
   ord(): 문자열을 아스키코드로 변환하는 함수'''

def solution(s):
    answer = True
    #아스키 코드를 이용해야겠다는 생각
    
    for c in s: #순차탐색을 하면서
        if 65 <= ord(c) <= 122: #아스키코드를 이용해 A~z안에 속하면 문자
            answer = False #문자가 하나라도 있다면 false로 바꾼다.
    
    return answer

