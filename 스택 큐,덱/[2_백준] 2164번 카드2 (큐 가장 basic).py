from collections import deque


n = int(input())

q = deque([i for i in range(1, n+1)]) # 123456


k = 0
while len(q) > 1:
    if k % 2 == 0:
        q.popleft()
    else:
        q.append(q.popleft())
    k += 1

print(q[0])
