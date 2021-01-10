s = input() # ex: 02984

result = int(s[0])

for i in range(1, len(s)):
    num = int(s[i])

    if num <= 1 or result <= 1: # 0 또는 1일 경우
        result += num
    else:
        result *= num

print(result)


# 본인은 0인 경우만 생각해 예외를 처리했는데 1의 경우는 생각하지 못했다.
# 1을 곱하는 것보다 더하는 것이 더 큰 수를 만들 수 있으니까.
