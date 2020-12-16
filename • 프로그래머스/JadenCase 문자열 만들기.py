# 첫 번째 나의 풀이 -> 정확성 43.8
def solution(s):
    ls = s.split()
    
    for i in range(len(ls)):
        ls[i] = ls[i][0].upper() + ls[i][1:].lower()
        # word[0] = word[0].upper() # 문자열 요소 변경불가라는 사실 잊지말기!!!
        #word[0].upper() + word[1:].lower() # word[i]가 아니라 ls[i]로 해야 됨!
        #print(word) # word만 바뀌고 ls 원본 자체는 안바뀜
    
    answer = ""
    for data in ls:
        answer += (data + " ")
        
    return answer.rstrip()




# 두 번째 다른 사람의 풀이 -> 테스트케이스 16만 미통과 상태
def solution(s):        
    return s.lower().title()
 