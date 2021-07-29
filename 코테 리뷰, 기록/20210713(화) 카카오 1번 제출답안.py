import math
def solution(money, minratio, maxratio, ranksize, threshold, months):
    answer = 0 #시민이 보유하게 될 최종 금액
    m = money
    k=0
    for a in range(months):
        #m = round(m, -2)

        m = str(m)[:-2] + '00'
        m = int(m) #백의자리 버리기
        print(m,'소유가정금액') # =소유 가정 금액
        max = False
        #소유 가정 금액 m
        if m < threshold:
            pass #세율 0퍼, m 그대로
        elif threshold <= m < (threshold+ranksize-1):
            m -= int(m*(minratio/100)) #minratio
        else:
            i=0
            while True:
                i+=1
                if minratio+i >= maxratio:
                    m -= int(m*(maxratio/100))
                    break

                if (threshold + i*ranksize) <= m < (threshold + (i+1)*ranksize - 1):
                    #세율: minratio+i
                    print((minratio+i),'세율-----')
                    m -= int(m*((minratio+i)/100)) ###여기가 메인
                    break   

        if int(str(m)[-2:]) != 0:
            k = int(str(m)[-2:])
        if str(m)[-3]=='9':
            m = round(m, -3)
        print(m,'한 달 차의 남은돈')
        print(k)


    answer = m +k
    return answer
