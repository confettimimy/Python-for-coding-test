ls = [int(input()) for _ in range(7)]

odd_ls = []
for num in ls:
    if num%2 != 0:
        odd_ls.append(num)

if len(odd_ls) == 0:
    print(-1)
else:
    print(sum(odd_ls))
    print(min(odd_ls))
