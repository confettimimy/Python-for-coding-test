a, b = map(int, input().split())

ls = []
for i in range(1, b+1):
    
    for _ in range(i):
        ls.append(i)

#print(ls)


sum = 0
for k in range(a-1, b-1+1):
    sum += ls[k]

print(sum)
