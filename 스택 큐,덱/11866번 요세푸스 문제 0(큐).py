from collections import deque

n, k = map(int, input().split())

result = []
q = deque([i for i in range(1, n+1)])


i=1
while True:
    if len(q)==0:
        break

    if i==k: # 3번째
        result.append(q[0])
        q.popleft()
        i=1
        continue

    # 뒤로 보낸다
    tmp = q.popleft()
    q.append(tmp)
    i += 1


#print(result)
result = list(map(str, result))
print("<" + ", ".join(result) + ">")


'''deque 덱 자료형을 이용해 문제 해결
   회전한다는 느낌으로, 회전큐 느낌, popleft()와 append() 이용 자유자재'''
