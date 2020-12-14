from collections import deque

def solution(n):

    # appendleft()를 이용하기 위해 / 수를 역순으로 넣기 위해 appendleft를 이용한다.
    # AttributeError: 'list' object has no attribute 'appendleft'
    # 리스트는 appendleft() 함수가 존재하지 않기 때문에 덱을 이용했다.
    q = deque([])
    
    for c in str(n):
        q.appendleft(int(c)) # leftappend가 아님

    # 리턴값 확인용 코드    
    print(q) # deque([5, 4, 3, 2, 1])
    print(list(q)) # [5, 4, 3, 2, 1]
    
    return list(q)
