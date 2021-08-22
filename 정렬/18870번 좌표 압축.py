n = int(input())
x = list(map(int, input().split()))

s = set(x)
#print(s)

new = sorted(list(s))

dic = dict()
cnt=0
for a in new:
    dic[a] = cnt
    cnt += 1
#print(dic) #설정 완료.



answer = []
for k in x:
    answer.append( dic[k] )

for p in answer:
    print(p, end=' ')
