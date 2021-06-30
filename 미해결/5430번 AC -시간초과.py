from collections import deque
import sys


t = int(sys.stdin.readline())

for _ in range(t):
    
    p = input()
    n = int(sys.stdin.readline()) #배열의 갯수    
    arr = sys.stdin.readline() #?
    
    if n == 0 or n == 1:
        print('error')
        continue
    
    arr = arr[1:-2]
    arr = list(map(int, arr.split(',')))
    #print(arr)


    q = deque(arr)
    #print(q)
    #print(list(q))
    
    chk = False
    r_count = 0 #시간문제를 해결하기 위한 뒤집기 함수 갯수
    for func in range(0, len(p)):

        if p[func] == 'R': #뒤집는 함수 실행
            r_count += 1
            '''q = list(reversed(list(q)))
            q = deque(q)'''
            #print(q,'1')
        elif p[func] == 'D': #첫 번째 숫자를 버리는 함수
            if len(list(q)) == 0:
                print('error')
                chk = True
                break
            
            if p[func-1] == 'R' and func!=0: #이전 함수가 R이라면 + 첫번째 함수명령이 아니라면
                q.pop() #오른쪽 것을 뺀다
            else:
                q.popleft()
            #print(q,'2')
                
    if chk == False:
        #print(list(q)) # [1, 2, 3, 5, 8] : X -> [1,2,3,5,8] : O 
        #print(q)
        if r_count%2==0:
            print( str(list(q)).replace(" ", "") )
        else: #r함수 등장 개수가 홀수개라면
            print( str(list(reversed(list(q)))).replace(" ", "") )


'''<시간초과 해결>
'''
