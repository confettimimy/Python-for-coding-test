import sys
sys.setrecursionlimit(1000000)


def dfs(v):
    visited[v] = True

    for e in graph[v]: # 연결된 노드 모두 탐색
        if not visited[e]:
            parents[e] = v # 부모노드 저장
            dfs(e)


n = int(input())

graph = [[] for _ in range(n+1)]# 인접리스트 방식

# 부모 저장용 (여기 처리가 중요한 관건이였음)
parents = [0 for _ in range(n+1)]

for _ in range(n-1): ###
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False]*(n+1)


for i in range(1, n+1):
    if not visited[i]:
        dfs(i)



# 결과 출력
# 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
for i in range(2, n+1):
    print(parents[i])

