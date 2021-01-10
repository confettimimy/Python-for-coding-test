''' • DFS 구현 시 스택 자료구조를 이용 -> 실제 구현은 재귀함수를 이용
    • BFS 구현 시 큐 자료구조를 이용 '''
# DFS의 경우 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작하지만, BFS는 그 반대이다.
from collections import deque


# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐의 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True ###[1]

    #큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True ###[1]


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
bfs(graph, 1, visited)


# [1] append하면 = 즉 값이 큐에 들어오면 방문처리 시키기!