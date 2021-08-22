s1 = input()
s2 = input()
s3 = input()


def func(s):

    before = s[0]
    result = []
    tmp = 1
    for i in range(1, len(s)):
        if before == s[i]: #2개 이상이라면 연속
            tmp += 1
        else:
            result.append(tmp)
            tmp = 1
        before = s[i]
        
    result.append(tmp) #마지막까지의 처리
    #마지막까지의 연속구간 tmp는 구해지고 result에는 append되지 않았을 경우
    #여기를 처리 안해줘서 틀렸었다. 여러 개 풀어보면서 생긴짬
    
    #print(result)
    return max(result)


print(func(s1))
print(func(s2))
print(func(s3))


