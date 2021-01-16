# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# -> 인접리스트 방식 이용
def dfs(v, visited, graph):
    visited[v] = True
    
    for e in graph[v]:
        if visited[e] == False:
            dfs(e, visited, graph)


def solution(n, computers):
    for c in computers:
        print(c)
    answer = 0
    
    graph = [[] for _ in range(n)]
    print(graph)
    for i in range( len(computers)):
        for j in range( len(computers[0])):
            if i == j: # 자기 자신과의 경우는 제외하기
                continue
            if computers[i][j] == 1: # 서로 연결돼있는 컴퓨터만
                graph[i].append(j)
                graph[j].append(i)
    print(graph)
    
    visited = [False]*(n)
    
    for k in range(n):
        if visited[k] == False: # 이 처리를 안해서 계속 틀리게 나온거였네 .. ㅡㅡ 시작점을 0으로 해야핳지 1로 해야할지의 문제가 아니라!!
            dfs(k, visited, graph)
            answer += 1
    
    return answer
