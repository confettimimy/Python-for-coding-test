n = int(input())

for i in range(1, n+1):
    ls = input().split()
    ls.reverse()

    number = "#"+str(i)+":"
    print("Case", number, " ".join(ls) )

