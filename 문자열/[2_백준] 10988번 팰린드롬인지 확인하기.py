s = input()

answer = 1

mid = (0+len(s)-1)//2

end = len(s)-1
for i in range(mid+1): # 'mid+1'로 설정해야 맞음
    if s[i] != s[end-i]:
        answer = 0

print(answer)
