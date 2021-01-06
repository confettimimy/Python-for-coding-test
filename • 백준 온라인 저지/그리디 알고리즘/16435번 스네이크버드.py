n, l = map(int, input().split())

h = list(map(int, input().split()))

h.sort()

for i in h:
    if i <= l:
        l += 1 # 과일 하나를 먹으면 길이가 1만큼 늘어난다.

print(l)
    
