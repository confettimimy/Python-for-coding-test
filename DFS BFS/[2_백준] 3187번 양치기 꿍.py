import sys
sys.setrecursionlimit(1000000)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):

    visited[x][y] = True

    global wolf, sheep

    if maps[x][y] == 'v': # 늑대라면
        wolf += 1
    elif maps[x][y] == 'k': # 양이라
        sheep += 1


    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]

        if 0 <= nx < r and 0 <= ny < c:
            if maps[nx][ny] != '#':
                if visited[nx][ny] == False:
                    dfs(nx, ny)



r, c = map(int, input().split())

maps = [ list(input())  for _ in range(r)] # input() -> list( input() ) 문자열 요소는 변경이 안되니까 리스트 자료형으로 만들어버리기

visited = [[False]*c for _ in range(r)]

wolf = 0
sheep = 0

answer = [0, 0]

for i in range(r):
    for j in range(c):

        if maps[i][j] != '#':
            if visited[i][j] == False:
                wolf = 0
                sheep = 0
                dfs(i, j)
                if wolf >= sheep:
                    answer[1] += wolf # 양 다 죽고, 살아남는 늑대의 수 기록하기
                elif wolf < sheep:
                    answer[0] += sheep

for a in answer:
    print(a, end=' ')
