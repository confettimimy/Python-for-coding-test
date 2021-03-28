n, m = map(int, input().split())

castle = []
for _ in range(n):
    castle.append( input() )
    

hang = [0]*n
yul = [0]*m


for i in range(n):
    for j in range(m):
        if castle[i][j] == 'X':
            hang[i] = 1
            yul[j] = 1


print(max( hang.count(0), yul.count(0) ))
