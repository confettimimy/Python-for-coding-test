def solution(s):
    answer = ''
    
    if len(s) % 2 == 0: #문자열 개수가 짝수인 경우
        answer = s[len(s)//2-1] + s[len(s)//2] #문자열 인덱싱 방법으로 접근
    else: #홀수인 경우
        answer = s[len(s)//2]
        print(answer)
    
    return answer


# TypeError: string indices must be integers 문자열 인덱스는 정수여야 합니다
# s[len(s)/2] -> s[len(s)//2] 로 해결.