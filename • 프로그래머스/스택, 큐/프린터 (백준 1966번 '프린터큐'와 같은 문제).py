from collections import deque
def solution(priorities, location):
    q = deque(priorities)
    for i in range(len(priorities)):#위치 기록해놓기
        q[i] = (q[i], i)
    #print(q)
    
    end = [] #처리된 순서대로 넣을거임 
    while True:
        if len(end) == len(priorities):
            break
        first = q[0][0]
        tmp = [q[k][0] for k in range(1, len(q))]
        status = False
        for after in tmp:
            if first < after: #뒤에 첫번째보다 우선순위가 더 중요한게 있다면
                save = q.popleft() #뒤로 보내버리기 
                q.append(save)
                status = True
                break #하나라도 있다면 시간지체하지말고 뒤로 보내버리기 
        if status == False: # first가 우선순위 제일 크다면 인쇄하기
            end.append(q[0]) #처리
            q.popleft()
    
    #print(q) #원본 비어있음 확인 
    # 인쇄처리된 순서대로 append돼있을것
    print(end)
    
    cnt = 0
    for j in range(len(end)):
        cnt += 1
        if end[j][1] == location:
            return cnt
    
