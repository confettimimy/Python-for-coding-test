n = input() # 0 <= n <= 99

if int(n) < 10:
    n = '0' + n

count = 0 # 더하기 사이클 수

# n = 26
'''
2 + 6 = 8  +1
6   8  14  +1
8   4  12  +1
4   2   6  +1
2   6   8 wow
'''
origin = n # 원래 수 저장해놓기

ls = []
while True:

    ls = [] # 초기화
    for i in n:
        ls.append(int(i))
            
    ls.append( int(str(sum(ls))[-1]) )
    #print(ls)

    ls.remove(ls[0])

    count += 1 # 더하기 사이클 수
    n = "".join(map(str, ls))


    if n == origin:
        break

print(count)
