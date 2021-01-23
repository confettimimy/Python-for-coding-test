n = input() # ex) 9998

set_num = [0 for _ in range(9)] # 0~8


for i in n:
    if int(i) == 6 or int(i) == 9:
        set_num[6-1] += 0.5
    else:
        set_num[int(i)-1] += 1



answer = max(set_num)

if answer - int(answer) == 0.5:
    answer +=1

print(int(answer))

'''반례: 69696'''
