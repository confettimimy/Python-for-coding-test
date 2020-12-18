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
    
