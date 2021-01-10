n = int(input())

for _ in range(n):
    line = input()

    sum = 0
    score = 0 #득점
    
    for c in line: # 문자 하나씩 꺼내기
        if c == 'O':
            score += 1
            sum += score
        else:
            score = 0 # 다시 0으로 셋팅
    print(sum)
