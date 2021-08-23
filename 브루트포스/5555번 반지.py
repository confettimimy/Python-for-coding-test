from collections import deque

target = input()
case = int(input()) #반지의 개수

answer = 0
for _ in range(case):
    s = input()

    q = deque(s)
    #print(q)

    status = False
    rotate_num = 0
    while True:
        #print("".join(list(q)))
        if target in "".join(list(q)):
            status = True
            break
        if rotate_num == len(q):
            break
        
        tmp = q.popleft()
        q.append(tmp)
        
        rotate_num += 1

        
    if status == False: #회전하는동안 한번도 target문자열을 찾지 못했다면
        pass
    elif status == True:
        answer += 1

print(answer)
