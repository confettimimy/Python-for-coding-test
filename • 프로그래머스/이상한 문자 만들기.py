def solution(s):
    # 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
    words = s.split(" ")
    answer = ""
    
    for word in words:
        
        for i in range(len(word)):
            if i%2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += " "

    return answer[:-1]
