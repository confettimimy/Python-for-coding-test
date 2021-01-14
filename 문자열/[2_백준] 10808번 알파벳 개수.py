s = input()

dic = {}
for i in range(97, 122+1): # 대문자의 범위
    dic[chr(i)] = 0
#print(dic)


for c in s:
    dic[c] += 1


# 출력
for cnt in dic.values():
    print(cnt, end=' ')
