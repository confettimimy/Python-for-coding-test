def solution(record):
    answer = [] #최종답 문자열들을 넣을 리스트
    actual = [] #식별 유저아이디
    
    for line in record:
        ls = []
        ls = line.split(" ")
        if ls[0] == "Enter": # "Enter uid1234 Muzi"
            actual.append( [ls[0], ls[1], ls[2]] )
            print(actual)
        elif ls[0] == "Leave": # "Leave uid1234" 이 경우 문자열의 형태가 좀 다름
            if len(actual)>=2:
                for k in range(len(actual)): #IndexError: list index out of range
                    print(actual[k][1])
                    
                    if actual[k][1] == ls[1]:
                        print(actual[k],'지워야할거')
                        #actual.remove(actual[k]) #여기가 문제


'''
리스트에서
특정값을 가진 값 제거 remove
요소 하나가 하나의 값이라면 문제 없지만 여러개로 구성됐을때는 조금 난해하다
여태 이러한 문제가 계속 걸렸었다
'''
