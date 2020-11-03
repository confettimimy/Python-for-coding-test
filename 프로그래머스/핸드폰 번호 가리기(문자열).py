def solution(phone_number):
    
    #뒤에서부터 순차탐색
    i = len(phone_number) #ex)11
    while True: #전번 수 만큼 돌리기
        if i == 0:
            break
            
        if len(phone_number)-4 < i <= len(phone_number):
            i -= 1
            continue
            
        '''phone_number[i] = '*' #오류 원인: 문자열은 immutable한 자료형이라 요소값 변경 불가'''
        i -= 1
        phone_number = phone_number[0:i] + '*' + phone_number[i+1:]

        
    return phone_number
