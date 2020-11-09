''' • DFS 구현 시 스택 자료구조를 이용
    • BFS 구현 시 큐 자료구조를 이용 '''


# DFS 메서드 정의
def dfs(graph, v, visitied):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
