from collections import deque

def bfs(start):
    count=0
    
    q = deque([start])
    visited[start] = True ###[1]

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True ###[1]
                count += 1
    return count


n = int(input())
m = int(input())

visited = [False]*(n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(1))

# [1] append하면 = 즉 값이 큐에 들어오면 방문처리 시키기!