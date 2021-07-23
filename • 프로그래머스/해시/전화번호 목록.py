def solution(phone_book):
    
    phone_book.sort()
    
    answer = True
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
            return False
    return answer


    
    ''' <효율성 4개중 2개 통과 못했던 풀이>
    for number in phone_book:
        tmp = list(phone_book)
        tmp.remove(number)
        for one in tmp: # tmp에서 하나씩 꺼내며
            if number in one[:len(number)]: #one[:len(number)] 이 처리 해주니까 정확성 100됨/ 그냥 one으로 하면 접두사가 아니라 중간에 겹치는 것까지 False 처리가 되기 때문에 틀리는 경우가 발생한다.
                return False
    return answer
    '''
