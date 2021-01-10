a = int(input())
b = int(input())
c = int(input())

s = str(a*b*c) # 17037300

dic = {}
for j in range(10): # 딕셔너리 초기화
    dic[j] = 0 


for i in s:
    dic[int(i)] += 1 # i는 현재 문자열이기 때문에 인덱싱하기 위해서는 반드시 int()를 해주어야함

for value in dic.values():
    print(value)

