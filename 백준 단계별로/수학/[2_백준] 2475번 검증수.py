serial_number = list(map(int, input().split()))


answer = 0

for i in serial_number:
    answer += i*i

answer %= 10

print(answer)
