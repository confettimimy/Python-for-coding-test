n = int(input())
twin = int(input())

array = [[] for _ in range(n + 1)]  # 0은 무시하기 위해
# [[], [], [], [], [], [], [], []]

for _ in range(twin): # 6번 돌아감, 입력받은 line수 만큼! 저기를 비워둘 수 있음.
    x, y = map(int, input().split())

    array[x].append(y)
    array[y].append(x)
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
'''graph = [
        [],
        [2,5], #1에 연결된 노드들
        [1,3,5],
        [2],
        [7],
        [1,2,6],
        [5],
        [4]
        ]
'''


visited = [1] # 1은 방문처리 해버리고
count = 0

def dfs(num):
    global count

    # '연결된' 노드를 탐색
    for i in array[num]:
        if i not in visited: # 방문하지 않았다면
            count += 1
            visited.append(i)
            dfs(i)


dfs(1) # 1부터 감염
print(count)


