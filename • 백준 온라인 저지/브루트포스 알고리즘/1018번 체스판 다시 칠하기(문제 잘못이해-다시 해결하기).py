n, m = map(int, input().split())

arr = []
for _ in range(n):
    s = input()
    arr.append(s)



count = 0

print(arr)

tmp = arr[0][0]

for i in range(len(arr)):
    
    for j in range(len(arr[i])):
        if j == 0: # i==0 and j==0이엿는데 다음과 같이 바꾸니 된다!
            continue
        
        if tmp == arr[i][j]: # 이전과 같다면 값을 바꿔주고 count +=1 시킨다.
            if tmp == 'W': # # 이전 값을 넣어둔다(다음 원활한 계산을 위해)
                arr[i] = arr[i][:j] + 'B' + arr[i][j+1:] # 문자열 요소 변경 불가능
            else:
                arr[i] = arr[i][:j] + 'W' + arr[i][j+1:]
            count += 1
        tmp = arr[i][j] # 현재 수를 다시 tmp에 넣어 셋팅

        
print(arr)

print(count)
