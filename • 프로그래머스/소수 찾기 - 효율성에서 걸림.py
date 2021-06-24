import math

def solution(n):
    count = 0
    for num in range(2, n+1): # 2부터 n까지의 모든 수를 확인하며
        
        if num == 2 or num == 3: #예외처리
            count += 1
            #print(num,'g')
            continue
            
        chk = True #초기화
        for i in range(2, int(math.sqrt(n))+1):
            if num%i==0:
                chk = False
                #break #효율성을 위해 가지치기. 한번이라도 f나오면 바로 소수아님 판정이니까
        if chk == True: # 여전히 True라면
            #print(num,'z')
            count += 1
            
    return count


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
'''
def solution(n):
    cnt = [True]*(n+1)
    c = 0
    for i in range(2, int(n**0.5)+1):
        if cnt[i]==True: # 만약 소수면
            for j in range(i+i, n+1, i):
                cnt[j] = False # 소수의 배수는 소수가 아님
    for i in range(2, n+1): # 소수 개수 카운트
        if cnt[i]:
            c+=1
    return c'''
