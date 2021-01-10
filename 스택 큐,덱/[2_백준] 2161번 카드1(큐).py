from collections import deque

n = int(input())

ls = [i for i in range(1, n+1)]
q = deque(ls)

garbage = [] # 버린 카드들

'''4 버리고 아래로 버리고 아래로
132'''

i = 0
while len(q) > 1:
    if i%2 == 0:
        garbage.append(q.popleft())
    else:
        q.append(q.popleft())
    i += 1
    #print(q) # 확인용


for g in garbage:
    print(g, end=' ')
print(q[0])

