#조건: 같은 문자 또는 숫자가 연속해서 2번 나타나면 안 된다.
#예시: 00, 11, 55, 66은 같은 숫자가 2번 연속해서 불가능하다

s = input()


before =''
char = 26
number = 10
answer = 1 #가능한 경우의 수

for c in s:
    
    if before != '' and before[-1] == c: #이전값이랑 현재문자와 같다면
        if c == 'c': #문자
            answer *= (char-1)
        elif c == 'd': #숫자
            answer *= (number-1)
            
    else: #다르다면
        if c == 'c': #문자
            answer *= char
        elif c == 'd': #숫자
            answer *= number

    # 이전값 저장해두기
    before += c # 문자열은 변경 불가능하니 [-1]로 요소 접근하기


print(answer)
    
