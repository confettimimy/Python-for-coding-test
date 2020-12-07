n = int(input())
out_time = list(map(int, input().split()))

out_time.sort() # 최소

result = []
tmp_sum = 0
for i in range(n):
    tmp_sum += out_time[i]
    result.append(tmp_sum)

print(sum(result))

'''TypeError: 'int' object is not callable
예약어를 변수명으로 사용해서 생기는 오류'''
