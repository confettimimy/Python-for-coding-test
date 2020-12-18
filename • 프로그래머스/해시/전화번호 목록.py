# 첫 번째 문제풀이 (채점 결과 - 정확성: 69.2  효율성: 0.0  합계: 69.2 / 100.0)
def solution(phone_book):
    answer = True
    
    for i in phone_book: # 기준
        
        for k in phone_book:
            if i == k: # 자기 자신과인 경우는 패스
                continue
            if i in k:
                answer = False
            
    return answer

# 두 번째 풀이 (Counter를 이용해보자)
