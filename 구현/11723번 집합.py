import sys
m = int(input())

s = set()
for _ in range(m):
    request = sys.stdin.readline().split()
    if len(request)!=1:
        request[1] = int(request[1])

    if request[0] == "add":
        s.add(request[1])
    elif request[0] == "remove":
        if request[1] in s:
            s.remove(request[1])
    elif request[0] == "check":
        if request[1] in s:
            print("1")
        else:
            print("0")
    elif request[0] == "toggle":
        if request[1] in s:
            s.remove(request[1])
        else:
            s.add(request[1])
    elif request[0] == "all":
        s = {i for i in range(1, 20+1)}
    elif request[0] == "empty":
        s = set()


    #check 연산이 주어질때마다, 결과를 출력한다.

        
'''시간초과 문제 해결
input -> sys.stdin.readline 으로 해서 시간초과를 해결했다.'''
