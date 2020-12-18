import collections

def solution(participant, completion):
    participant.sort()
    completion.sort()

    '''# 확인용 코드
    print(collections.Counter(participant))
    print(collections.Counter(completion))
    print(collections.Counter(participant) - collections.Counter(completion))'''
    
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    return list(answer)[0]
    
# 동명이인이 존재할 수 있다고 문제에서 명시했기 때문에 특정한 이름을 가진 사람의 수를 담는, 'mislav': 2 이러한 key-value값 형태의 해시 및 딕셔너리 자료형을 이용하는 것이 유도되는 문제이다.
