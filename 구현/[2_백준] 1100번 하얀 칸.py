chess = [input() for _ in range(8)]

horse_count = 0


for i in range(8):
    for j in range(8):
        
        if i%2 == 0: # 하얀 칸 찾기 1
            if j%2 == 0:
                if chess[i][j] == 'F':
                    horse_count += 1
        elif i%2 != 0: # 하얀 칸 찾기 2
            if j%2 != 0:
                if chess[i][j] == 'F':
                    horse_count += 1

                    
print(horse_count)
