def solution(answers):
    #print(len(answers))
    counts = [0, 0, 0]
    
    ls1 = [1, 2, 3, 4, 5]
    ls2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ls3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(0, len(answers)):
        if answers[i] == ls1[i%5]:
            counts[0] += 1
        if answers[i] == ls2[i%8]:
            counts[1] += 1
        if answers[i] == ls3[i%10]: #모두 ls1로해서 틀렸었음 
            counts[2] += 1
    
    
    final = [[1], [2], [3]]
    for k in range(3):
        final[k].append(counts[k])
        
    final.sort(key=lambda x: x[1], reverse = True)
    
    answer = []
    answer.append(final[0][0])
    for b in range(1,3):
        if final[0][1] == final[b][1]:
            answer.append(final[b][0])  
    return answer

# 미해결 -> 해결완료!
