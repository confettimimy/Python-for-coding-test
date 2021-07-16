import math

def solution(dartResult):
    answer = 0

    num = 0
    score = []
    for i in range(len(dartResult)): # 1S2D*3T
        if dartResult[i].isdigit():
            if dartResult[i] =='1' and dartResult[i+1] =='0':
                num = 10
                continue
            if i!=0 and dartResult[i-1]=='1':
                continue #아래 num값 바꾸지않기 
            num = int(dartResult[i]) #계속 업데이트됨
        
        elif dartResult[i].isalpha():
            if dartResult[i]=='S':
                score.append(int(math.pow(num, 1)))
            elif dartResult[i]=='D':
                score.append(int(math.pow(num, 2)))
            elif dartResult[i]=='T':
                score.append(int(math.pow(num, 3)))
        elif dartResult[i]=='*':
            if len(score)==1:
                score[-1] = score[-1]*2
            else:
                score[-1] = score[-1]*2
                score[-2] = score[-2]*2
        elif dartResult[i]=='#':
            score[-1] = -(score[-1])
        
    #print(score)
    #print(sum(score))
    return sum(score)
