x, y = map(int, input().split())

first_area = [1, 3, 5, 7, 8, 10, 12]
second_area = [4, 6, 9, 11]
# 총 몇일이 흘렀는가?
sum = 0
for month in range(1, x): # 1월부터 x월 전까지
    if month in first_area:
        sum += 31
    elif month in second_area:
        sum += 30
    elif month == 2:
        sum += 28

sum += y
sum -= 1

# print(sum) # 확인


yoil = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print( yoil[sum%7] )
