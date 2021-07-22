'''나는 계속 한 길로만 감.@@@@@@@@@ 여태 dfs 골드문제 풀 때 계속 걸렸었던 문제.
그렇게 가도 맞긴 한건데, '최대'길이는 아님.
한 길로만 쭉 가고. 그 외의 가능성도 탐색해야하는데
max(ans, cnt)비교하며 최대일때 실행하는 걸로 가야하는데 그게 안됨 지금

<<dfs함수의 매개변수를 이용하는 방식>>으로 문제해결 dfs(x, y, s)-> 여기서의 매개변수 s
다만 이제 시간초과의 문제가 발생 --> PyPy로 제출해서 꾸역꾸역 되다가 또멈춤'''
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, s):

    global ans
    
    ans = max(ans, len(s))
    #print(s)

    global visited
    visited[x][y] = True
    
    
    for a in range(4): #a=0 깊이 걸리면 나머지 a가 1, 2, 3일때 탐색 안하는게 아님. 모두 다 탐색한다
        nx = x + dx[a]
        ny = y + dy[a]

        if 0<=nx<r and 0<=ny<c:
            if visited[nx][ny] == False:
                #새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
                if board[nx][ny] not in s:
                    #visited[nx][ny] = True ###
                    dfs(nx, ny, s+board[nx][ny])
                    visited[nx][ny] = False### 이 처리를 꼭 해줘야함. 위에서 깊이있게 쭉 가고 그 한줄이 끝나면  또 다른줄이 뻗어나가야하니까 visited 다시 초기



r, c = map(int, sys.stdin.readline().split())
board = []
for _ in range(r):
    board.append(sys.stdin.readline())

visited = [[False]*c for _ in range(r)]

ans = 0 #최종

dfs(0, 0, board[0][0])


print(ans)
