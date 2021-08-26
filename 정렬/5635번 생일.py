n = int(input())

ls = []
for _ in range(n):
    ls.append(input().split())
#print(ls)


ls.sort(key=lambda x:(int(x[3]), int(x[2]), int(x[1])))
#print(ls)



print(ls[-1][0])
print(ls[0][0])
