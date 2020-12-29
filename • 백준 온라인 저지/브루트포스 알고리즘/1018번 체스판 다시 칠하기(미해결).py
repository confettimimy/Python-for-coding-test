n, m = map(int, input().split())

arr = []
for _ in range(n):
    s = input()
    arr.append(s)



count = 0

print(arr)

tmp = arr[0][0]

for line in arr:
    
    for i in range(m):
        if tmp == arr[i]: # 이전과 같다면 값을 바꿔주고 count +=1 시킨다.
            if tmp == 'W':
                i = 'B' # 이전 값을 넣어둔다(다음 원활한 계산을 위해)
            else:
                i = 'W' ### 이거 자체가 arr원본 자체를 못바꿔서 그런것인가? ### 다시 생각해보니 문자열 요소는 변경 불가능...
            count += 1
            
        tmp = i # 현재 수를 다시 tmp에 넣어 셋팅
print(arr)

print(count)
