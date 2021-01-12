
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    visited[x][y] = True

    for p in range(4):
        nx = x + dx[p]
        ny = y + dy[p]

        if 0 <= nx < n and 0 <= ny < m: ### [1] n, m 절대 헷갈리지 말 것!
            if maps[nx][ny] == 0 and visited[nx][ny] == False:
                dfs(nx, ny)


n, m = map(int, input().split())

maps = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

icecream_cnt = 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0 and visited[i][j] == False:
            dfs(i, j)
            icecream_cnt += 1

print(icecream_cnt)


'''[1]
if maps[nx][ny] == 0 and visited[nx][ny] == False:
IndexError: list index out of range
내 방식대로 풀었더니 왜 이 오류가 날까..?

-> if 0 <= nx < n and 0 <= ny < m: 여기서 n과 m을 바꾸어 써서 틀린거였음.



(0,0)(0,1)(0,2)(0,3)(0,4)
(1,0)(1,2)(1,3)(1,4)(1,5)
(2,0)(2,1)...
(3,0)...

-> 이중포문 상에서는 (i, j)의 인덱스 모습이 이렇게 흘러감!



만약 현재 위치(0,0)에서 (1,0)을 이동시키면 x값이 이동돼 당연히 오른쪽으로 한칸 이동하는거라고 잘못 생각하고 있었다.
이동 후 위치(1,0)은 아래로 한 칸 내려간 것이다!!!



방향배열에서 대각선 추가해 런타임 에러난 문제들도 이것들 때문에 인덱스 아웃에러가 났던 것인가? 꼭 다시 확인해보기
-> (2021/01/12) 그렇다. 대각선 요소 추가한 문제를 살펴보니 또 여기서 문제가 났었다.
   앞으로 범위 내에 있는지의 조건을 정의할 때 m과 n을 바꿔쓰지 않도록 주의하자.'''
