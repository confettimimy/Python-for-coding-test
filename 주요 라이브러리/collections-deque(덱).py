# 보통 파이썬에서는 Ddeque를 사용해 큐를 구현한다
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print('1', data)
print('2', list(data))

data.pop()
data.popleft()

print('3', data)
print('4', list(data))
