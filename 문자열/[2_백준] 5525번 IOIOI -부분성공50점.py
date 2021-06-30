import sys
n = int(input())
m = int(input())
s = sys.stdin.readline()

#Pn = n개의 O, n+1개의 I
pn = 'I'
pn += ('OI'*n) #위에서 n이 주어진다.

count = 0

#참고로 겹쳐도 된다.
for i in range( 0, len(s)-len(pn)+1 ):
    #하나의 케이스
    status = True

    cnt = len(pn) # 3
    a = 0
    while cnt>0 and a<len(pn):                             # and s[i+1] == pn[i+1]... pn의 개수만큼 
        #print(s[i+a], pn[len(pn)-cnt],'확인')
        if s[i+a] != pn[len(pn)-cnt]:
            status = False
        cnt -= 1
        a += 1

    if status == True: #위 while문에서 한번도 False된적이 없다면
        count += 1



print(count)


