'''
<필요 역량>
dfs구현할 줄 아느냐 + 조합 구현

<문제 풀이 과정>
1. 주어진 연구소에서 3개의 벽을 선택한다.
- 조합(Combination) 사용
2. 벽이 선택된 연구소에 바이러스를 퍼트린다.
- BFS or BFS 사용
3. 바이러스가 퍼지지 않은 안전지역의 갯수를 구한다.'''
from itertools import combinations
import copy


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y): #바이러스 퍼뜨리는 함수
    
    global visited
    visited[x][y] = True
    
    global maps_copy #maps원본을 사용해버리면 원본을 바꾸어버린다. global을 사용해서 현 사용되고있는 복사본 maps_copy의 값을 바꾸도록 하자.
    maps_copy[x][y] = 2 #바이러스로 바꾼다.

    for a in range(4):
        nx = x + dx[a]
        ny = y + dy[a]

        if 0<=nx<n and 0<=ny<m:
            if visited[nx][ny] == False:
                if maps_copy[nx][ny] != 1 and maps_copy[nx][ny] == 0:  #다음 갈 곳이 '벽'이 아니고 빈 공간이라면
                    dfs(nx, ny)
                    


n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

visited = [[False]*m for _ in range(n)]

possible = []



zero_place = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            zero_place.append((i, j))

for case in list(combinations(zero_place, 3)): # [1] 빈 공간 3개를 고른다.
    #print(case)
    # maps를 복사해서 사용해야한다. 원본 maps를 사용하면 계속 maps값이 바뀌게되니..
    # 3개의 벽을 세우는 경우의 수 마다 maps 변경을 하므로 원본 maps를 deepcopy한 maps_copy 를 변화시킨다.
    maps_copy = copy.deepcopy(maps)
    visited = [[False]*m for _ in range(n)]
    
    maps_copy[case[0][0]][case[0][1]] = 1 #벽 3개를 세운다.
    maps_copy[case[1][0]][case[1][1]] = 1
    maps_copy[case[2][0]][case[2][1]] = 1

    # 이제 2 바이러스를 퍼뜨린다.
    for i in range(n):
        for j in range(m):
            if maps_copy[i][j] == 2:
                dfs(i, j) # 어디서부터 시작? = 바이러스가 있는곳(2)이면 시작
                
    # 이제 바이러스가 퍼졌다. 이제 안전영역의 크기 구하기.
    # 지도에서의 0의 갯수
    safe = 0
    for i in range(n):
        for j in range(m):
            if maps_copy[i][j] == 0:
                 safe += 1
    possible.append(safe)


#print(possible)
print(max(possible))


'''<문제풀이 후기>
위에 기술한 문제풀이 과정의 구조만(문제를 어떤식으로 접근해야할지) 참고한 뒤,
나머지는 모두 스스로의 힘으로 풀었다. dfs 구현할 줄 알고 + 3개 벽 세울때의 조합 사용까지,
그리고 깊은복사 개념을 이용해 maps의 복사본을 사용해야겠다는 생각과 + global의 사용법까지.
이미 알고있는 것을 확실히 파악한 느낌이다.

dfs구현과 조합 개념이 이렇게 같이 쓰일 수가 있구나..
삼성은 <조합+조합> 이라든지 <dfs+조합> 이라든지 문제를 풀다보면 두가지 이상을 섞는 느낌이 크다.

다만 처음에 문제를 풀 때 어떠한 접근으로 풀이해야할지에 대한 구조 파악 (일련의 단계?)은 더 연습을 해야겠다.

참고로 이전에 리스트의 깊은복사를 위해
copy = list(ls)
다음과 같이 사용했는데, 이번에는 이중리스트를 복사해야하니 copy라이브러리의 deepcopy(arr)와 같이 사용하는 것이 좋은 것 같다.
이런 라이브러리도 있었구나를 잘 알아두자.
'''
