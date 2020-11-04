def solution(s):
    answer = ''
    
    array = list(map(int, s.split()))
    answer = str(min(array)) + ' ' + str(max(array))
    
    return answer
