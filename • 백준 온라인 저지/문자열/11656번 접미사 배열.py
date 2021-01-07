s = input()

j = []

for i in range(len(s)):
    j.append(s)
    s = s[1:] # 문자열 요소 변경 불가능, 문자열 인덱싱 및 슬라이싱은 가능.

j.sort()

for one in j:
    print(one)
