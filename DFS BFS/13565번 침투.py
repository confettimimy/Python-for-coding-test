import sys
sys.setrecursionlimit(1000000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def percolate(x, y):
    visited[x][y] = True
    maps[x][y] = '3' # '0'을 '3'으로 바꾼다. 
    
    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]

        if 0 <= nx < m and 0 <= ny < n:
            if maps[nx][ny]=='0' and visited[nx][ny]==False:
                percolate(nx, ny)



m, n = map(int, input().split())
maps = []
for _ in range(m):
    maps.append(list(input()))
#print(maps)

visited = [[False]*n for _ in range(m)]



for i in range(m):
    for j in range(n):
        if i==0: #or i==m-1 or j==0 or j==n-1: # 바깥쪽이면=위쪽에서 dfs침투 시작
            #print((i, j))
            percolate(i, j)

#for line in maps:
#    print(line)

answer = 'NO'
for k in range(n):
    if maps[m-1][k] == '3': #위에서 흘려준 전류가 아래쪽까지 잘 전달되면(아래중 한곳이라도)
        answer = "YES"
        break

print(answer)


'''문제를 약간 잘못이해해서 약간 헷갈렸다.
   바깥쪽에서 흘려보낸 전류 = 가장 맨 위의 행에서 흘린 전류
   안쪽까지 잘 침투된지 확인 = 아래 부분이 안쪽을 뜻함
   맨 아래 행 모두에 침투되어야 한다는 것이 아님! 예제를 보면 모두 침투되지 않아도 맨아랫행 한곳이라도 침투되면 안까지 침투되었다고 판단하고 있음
   문제를 약간 잘못 이해!'''
