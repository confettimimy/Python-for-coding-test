n = int(input())
arr = list(map(int, input().split()))

m = max(arr)

for i in range(len(arr)):
    arr[i] = arr[i]/m*100  # a = a/m*100 <- 이렇게 하면 배열 arr 원본값이 바뀌지 않는다!!!

print( sum(arr)/len(arr) )
