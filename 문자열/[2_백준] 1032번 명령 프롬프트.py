n = int(input())

answer = input()
for _ in range(1, n):
    s = input()
    for i in range(len(s)):
        if s[i] == answer[i]:
            pass
        else:
            answer = answer[:i] + "?" + answer[i+1:] # 문자열 요소 변경 불가

print(answer)   
