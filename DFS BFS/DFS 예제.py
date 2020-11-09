''' • DFS 구현 시 스택 자료구조를 이용
    • BFS 구현 시 큐 자료구조를 이용 '''


# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)



# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8], # 노드1과 연결돼 있는 노드들
    [1, 7], # 노드2에 연결돼 있는 노드들
    [1, 4, 5], # 노드3에 연결돼 있는 노드들
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9
# [False, False, False, False, False, False, False, False, False]

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
