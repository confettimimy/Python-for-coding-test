t = int(input())

for _ in range(t):
    s = input()

    ls = s.split(" ")
    #print(ls)

    new_ls = []
    
    for one in ls:
        one = list(one)
        one.reverse() # 문자열은 reverse() 불가능
        one = "".join(one)
        new_ls.append(one)

    for pr in new_ls:
        print(pr, end=' ')
    print('')

