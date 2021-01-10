n = int(input())
plans = input().split()

x, y = 1, 1

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'D', 'U'] # (dx, dy)와 move_types는 대응돼야 함! 아래 for문 i 수행 시 같도록.
# (내가 생각한 방향과 달라서 틀렸었음)

for plan in plans:
    
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n: # 1 <= nx,ny <= n
        continue

    x = nx
    y = ny


print(x, y)
