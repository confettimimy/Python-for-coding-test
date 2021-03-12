n, m = map(int, input().split())


dic = {}

for _ in range(m):
    i, j, k = map(int, input().split())

    a = i
    while i <= a <= j:
        dic[a] = k
        a+=1


#공이 들어있지 않은 바구니는 0을 출력한다.
for e in range(1, n+1):
    if e not in dic.keys():
        dic[e] = 0


# 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력       
for w in range(1, len(dic)+1):
    print(dic[w], end=' ')
    
