def solution(line1, line2):
    answer = 0
    target = line2
    while True:
        #print(target)
        if len(target) > len(line1):
            return answer
        # 첫번째는 target으로 시작, target = "bbb"
        for i in range(0, len(line1)-len(target)+1): #abbbcbbb
            status = True
            tmp = i
            tmp2=0
            while True:
                if tmp2 == len(target):
                    break

                if target[tmp2]=='_':
                    pass
                elif line1[tmp] != target[tmp2]:
                    status = False
                tmp+=1
                tmp2+=1

            if status == True: #여전히 true라면
                answer+=1
                #print(i,'정답 시작점 확인')
        target = "_".join(list(target))

    return answer
