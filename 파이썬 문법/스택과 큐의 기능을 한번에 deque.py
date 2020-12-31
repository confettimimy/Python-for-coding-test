'''deque는 스택과 큐의 기능을 모두 가진 객체로 출입구를 양쪽에 가지고 있다.
   즉 스택처럼 써도 되고, 큐처럼 써도 된다!'''

from collections import deque


q = deque('love')
print(q)
'''deque(['l', 'o', 'v', 'e'])'''



# 1. 스택 구현: append(), pop()
q.append('m')
print(q)
'''deque(['l', 'o', 'v', 'e', 'm'])'''

q.pop()
print(q)
'''deque(['l', 'o', 'v', 'e'])'''



# 2. 큐 구현: append(), pop(), appendleft(), popleft()
q.appendleft('l')
print(q,'zz')
'''deque(['l', 'l', 'o', 'v', 'e'])'''

q.appendleft(q.pop())
print(q)
'''deque(['e', 'l', 'l', 'o', 'v'])'''

q.popleft()
print(q)
'''deque(['l', 'l', 'o', 'v'])'''


