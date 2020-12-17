a, b = input().split()

a= list(a) # a = ['7', '3', '4']
b= list(b)

a.reverse() # a = ['4', '3', '7']
b.reverse()

a = int("".join(a)) # a = "437"
b = int("".join(b))

if a>b:
    print(a)
else:
    print(b)
