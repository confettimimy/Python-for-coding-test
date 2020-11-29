import sys
sys.setrecursionlimit(10000) # [1] (재귀한계를설정한다)


def dfs(v):
    visited[v] = True # 현재 노드를 방문 처리
    for e in graph[v]: # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        if not visited[e]: 
            dfs(e)
            #visited[e] = True #쓰지말것!! -> 바로 윗줄 재귀함수 실행하면 어차피 연결된 그 해당 노드(e)도 dfs함수 호출 후 첫번째줄에서 방문처리 될거니까.


n, m = map(int, sys.stdin.readline().split()) # [2] 빠르게 입력받기 위해 input()을 sys.stdin.readline()으로 대체

graph = [[] for _ in range(n+1)] # 인접 리스트 방식
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split()) # [2]
    graph[x].append(y)
    graph[y].append(x)

visited = [False]*(n+1)

count = 0 # 연결 요소의 개수

for i in range(1, n+1): # 모든 노드를 순회하며 시작점이 가능한 곳을 찾는다. 시작점으로 가능하면 dfs수행.
    if not visited[i]:
        count += 1
        dfs(i)
'''일단 시작점으로 한 번 걸리면 dfs()함수 호출해서 그 시작점과 연결된 노드까지 모두 탐색하게 될거임.
   그 시작점과 연결된 노드들도 모두 방문처리되어 있을거니 넘어갈거고
   그리고 바로 이전 연결선과 연결되지 않은 또다른 새로운 시작점 ~반복.
''' 

print(count)

# [1] 런타임 에러 발생 이유: python은 재귀제한이 걸려있기 때문에 재귀 허용치가 넘어가면 런타임에러가 발생한다.
# 기본적으로 설정돼 있는 최대 재귀 깊이는 1,000이다. 따라서 상단에 sys.setrecursionlimit(10000)을 써주어야 한다.

# [2] 시간 초과 문제: 빠르게 입력받기 위해 input()을 sys.stdin.readline()으로 대체

# 추가 설명: 모든 요소가 연결되어 있다면, count의 값은 1로 출력될 것이다.

# DFS와 인접리스트를 이용해 푼 문제
