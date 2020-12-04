now_location = input()

### 여기를 어떻게 해야할지 고민했었음.
x = ord(now_location[0]) # 문자를 아스키코드 숫자로 변환 
# a = 97
x = (x - 97) + 1


y = int(now_location[1]) # 문자열 인덱싱 접근


moving_case = [(2,-1), (-2,-1), (2,1), (-2,1), # 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하는 경우
               (-1,-2), (1,-2), (-1,2), (1,2)] # 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하는 경우

count = 0

for case in moving_case:
    # 이동 후 위치
    x += case[0]
    y += case[1]
    
    # 이동 후 위치가 맵 범위 내에 있다면
    if 1 <= x <= 8 and 1 <= y <= 8:
        count += 1

    # x, y 다시 원위치 해줘야함 <- 간과해서 틀렸던 부분
    x -= case[0]
    y -= case[1]

print(count) # 이동할 수 있는 경우의 수

