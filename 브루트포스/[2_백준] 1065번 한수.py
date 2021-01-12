n = int(input()) # 1 <= n <= 1000
count = 0


for number in range(1, n+1):

    # 파악해보니 한 자리 수, 두 자리 수는 모두 '한수'라고 할 수 있음.
    if 1 <= number < 100:
        count += 1

    elif 100 <= number < 1000: # 세 자리수 일때
        s = str(number) # ex: 987
        if (int(s[0]) - int(s[1])) == (int(s[1]) - int(s[2])): # 등차수열이라면
            count += 1
        
    elif number == 1000:
        pass

print(count)
