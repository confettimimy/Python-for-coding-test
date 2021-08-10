ls = []
for i in range(1,8+1):
    score = int(input())
    ls.append( [i, score] )

ls.sort(key=lambda x:x[1], reverse=True)



sum = 0
for j in range(5):
    sum += ls[j][1]

new = []
for k in range(5):
    new.append(ls[k][0])

new.sort()

print(sum)
for n in new:
    print(n, end=' ')
