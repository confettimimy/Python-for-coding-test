def solution(phone_book):
    phone_book.sort(key=lambda x:len(x)) #시간단축을 위한 정렬 작업 - 그럴수록 더 빨리 찾고 return해버리니까 
    
    answer = True
    for number in phone_book:
        tmp = list(phone_book)
        tmp.remove(number)
        for one in tmp: # tmp에서 하나씩 꺼내며
            if number in one[:len(number)]: #one[:len(number)] 이 처리 해주니까 정확성 100됨 
                return False
    return answer


'''효율성 2개만 통과하면됨 '''
