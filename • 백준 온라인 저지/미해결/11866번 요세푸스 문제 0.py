from collections import deque

n, k = map(int, input().split()) # 7, 3

q = deque([i for i in range(1, n+1)])
arr = []

'''
124567
3
'''

count = 1
while q:
    if count % 3 == 0:
        arr.append(q.popleft())
    else: ###
        pass

    count += 1

print(arr)
    
