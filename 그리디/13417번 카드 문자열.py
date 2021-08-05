from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    ls = list(input().split())


    # 태욱이는 가장 왼쪽에 있는 카드부터 차례대로 한 장씩 가져올 수 있다.
    q = deque([ls[0]]) # [M]

    #어차피 사전순으로 가장 빠른 문자열만 찾으면된다
    #ls에 있는 문자열 중 m보다 작은것은 앞에 넣고, m보다 큰것은 뒤에 넣는다.
    save = ls[0]
    del ls[0]
    for c in ls: #하나씩 꺼내면서
        if ord(c) <= ord(list(q)[0]):
            q.appendleft(c)
        else:
        #elif ord(c) >= ord(list(q)[-1]):
            q.append(c)

            
    #print(q)
    print("".join(list(q)))

'''B A C A B A C 가 있다면
   맨 처음 B는 먼저 빼고,
   'B'를 중심으로 이것보다 작으면 앞에 넣고, 크면 뒤에 넣었는데
   'B'가 아니라 맨 앞(값이 항상 변함)을 기준으로 삼아야함.
   맨 앞 값보다 큰게 와버리면 사전순 바로 밀려버리니까

   그리디 + 덱 문제 
'''
    
