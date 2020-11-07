def solution(s):
    answer = False
    
    # str.isdigit()를 이용한 더 효율적인 방식
    if s.isdigit() == True and (len(s) == 4 or len(s) == 6):
        answer = True
    
    return answer


''' 
(1) 테스트케이스 5, 6이 통과되지 못했던 이유: 문제 조건의 '문자열 s의 길이가 4 혹은 6이고,'를 간과
(2) 순차탐색, 아스키코드를 이용하는 방식을 떠올려 문제를 풀었지만 str.isdigit()과 같이 간단한 함수가 있다는 사실을 잊고 있었다.

* 참고
chr(): 아스키코드를 문자열로 변환하는 함수
ord(): 문자열을 아스키코드로 변환하는 함수
'''