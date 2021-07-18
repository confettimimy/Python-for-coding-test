def solution(s): # baabaa /   a    a
    stack = []
    # stack = ba
    for i in range(len(s)):
        if len(stack)>=1 and stack[-1] == s[i]: #len(stack)>=1 조건 안달아서 range out 오류난거였음
            stack.pop()
        else:
            stack.append( s[i] )
    #print(stack)
    
    if len(stack)==0:
        return 1
    else:
        return 0

# 시간초과 문제 -> stack을 '문자열'말고 '리스트' 자료형으로 바꿔 접근해 시간초과 문제 해결
