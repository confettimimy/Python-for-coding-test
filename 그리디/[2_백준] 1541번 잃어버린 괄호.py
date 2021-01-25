s = input().split('-') # 55-50+40

#print(s)
s1 = []
for t in s:
    temp = list(map(int, t.split('+')))
    s1.append(sum(temp))
#print(s1,'확인')

result = s1[0]
for p in s1[1:]:
    result -= p
    
print(result)




'''eval() 사용 시 오류 이유; eval()에 "012"같은 것은 들어갈 수 없다.
   문제에서는 '수는 0으로 시작할 수 있다'고 명시해놓았다.
   -> eval()을 사용하지 않고 다시 풀어보자.'''
'''
<+ 틀렸던 첫 번째 풀이>
result = int(eval(s[0]))
for one in s[1:]:
    result -= int(eval(one))

print(result)

'''
