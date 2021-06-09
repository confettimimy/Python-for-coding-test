

while True:
    n = int(input())

    if n == 0:
        break

    # 정사각형 1x1 2x2 3x3 ...
    # n=1 -> 1
    # n=2 -> 2*2 + 1*1
    answer = 0
    for i in range(1, n+1):
        answer += i*i

    print(answer)

    
