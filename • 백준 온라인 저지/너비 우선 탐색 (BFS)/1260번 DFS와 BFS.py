from collections import deque


def dfs(v): # 궁굼증) graph 매개변수로 꼭 안받아도 되나..?
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


def bfs(v):
    queue = deque([v]) #요소 하나라도 들어가있어야 while루프를 시작할 수 있음
    visited[v] = True

    while queue:
        v = queue.popleft() #맨 앞에 있는 요소를 '빼서'
        print(v, end=' ')
        for i in graph[v]: #해당 요소에 연결된 요소들을 모두 'append'시킨다
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
    
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


for i in graph: ###
    i.sort()
# 문제2) 방문할 수 있는 정점이 여러 개일 때 정점 번호가 작은 것을 먼저 방문한다는 것을 놓치고 제출했다가 틀렸었다.
# [문제조건] '단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문'
 
 
visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
# 문제1) 여기 때문에 틀린 거였음 -> 똑같은 visited리스트를 이용했기 때문에. 즉 bfs함수호출은 변형된 값의 visited를 썼던 것.
 
 
 