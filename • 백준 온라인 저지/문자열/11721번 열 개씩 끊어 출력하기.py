N = input()

count = 10
for i in N:
    if count ==0:
        print()
        count = 10
    print(i, end='')
    count -= 1
