# DFS, '인접행렬' 방식
import sys


# 인접행렬 방식 -> 방향배열 / 대각선으로도 연결 가능
dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]

def solution(n, computers):
    
    network_cnt = 0
    
    visited = [[False]*n for _ in range(n)]
    
    
    
    def dfs(x, y):    
        visited[x][y] == True

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n:
                if computers[nx][ny]==1 and visited[nx][ny]==False:
                    sys.setrecursionlimit(10**6+190000)
                    dfs(nx, ny)                
    
    
        
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and visited[i][j] == False:
                dfs(i, j)
                network_cnt += 1
    
    
    return network_cnt

