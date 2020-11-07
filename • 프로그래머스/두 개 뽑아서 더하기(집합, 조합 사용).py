'''※ 중복을 허용하지 않는 set의 특징은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용하기도 한다.'''
from itertools import combinations

def solution(numbers):
    answer = [] 
    # a+b나 b+a는 같다 - 즉 순서 중요X - 조합 사용
    
    for case in combinations(numbers, 2):
        #print(case) #튜플로 나옴
        answer.append(case[0]+case[1])

    answer = set(answer) #집합 자료형을 사용해 중복 제거
    answer = sorted(list(answer)) #다시 리스트 자료형으로 변환해 오름차순으로 정렬    
        
    return answer

