import math
from collections import Counter

a, p = map(int, input().split())

d = [a]
cnt=0
while True:
    cnt+=1
    if cnt==100:
        break
    if d[-1]==a and len(d)>1:
        break

    sum = 0
    for c in str(d[-1]):
        sum += int( math.pow(int(c), p) )
    d.append(sum)

#print(d)


answer = 0
dic = dict(Counter(d))
for num in dic.keys():
    if dic[num] == 1:
        answer += 1
    else:
        break #1이 아닌거 나오면 바로 루프아웃. 시간효율을 위해
print(answer)
