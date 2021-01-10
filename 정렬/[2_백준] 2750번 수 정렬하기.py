n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort() #원본을 바꿔버림

for i in range(n):
    print(arr[i])
