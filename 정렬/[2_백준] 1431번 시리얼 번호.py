n = int(input())

ls = []
for _ in range(n):
    ls.append(input())



for i in range(n):
    ls[i] = [ ls[i], len(ls[i]) ]




i = 0 
for one_case in ls:
    serial_num = one_case[0]

    sum = 0
    for c in serial_num:
        if c.isdigit():
            sum += int(c)
    ls[i].append(sum)
    i += 1

#print(ls)



ls = sorted(ls, key=lambda x:(x[1], x[2], x[0]) )



# 결과 출력
for p in ls:
    print(p[0])
 
