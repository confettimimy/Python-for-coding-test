s = input()
target = input()

visited = [False]*len(s)  #중복되지 않는 것이 중요한 문제 !
#print(visited)

answer = 0 #등장횟수
for i in range(0, len(s)-len(target)+1):
    #print(s[i : i+len(target)])
    
    if s[i : i+len(target)] == target:
        
        status = False
        for q in range(i, i+len(target)):
            if visited[q]==True:
                status = True
                
        if status==False: #모두다 방문된적 없다면
                    
            answer += 1
            for k in range(i, i+len(target)):
                visited[k] = True

print(answer)
