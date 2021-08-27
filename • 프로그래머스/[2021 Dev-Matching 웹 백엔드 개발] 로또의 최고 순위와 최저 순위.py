def solution(lottos, win_nums): #민우 로또 번호, 당첨 번호
    score = 0 #고정점수 = 항상 일치 개수
    copy = list(win_nums)
    for i in range(len(lottos)):
        if lottos[i] in copy:
            #print(copy,'copy')
            score += 1 
            copy.remove(lottos[i])
    #print(score)
    
    
    answer = []
    copy_cnt = len(copy)
    max_score = score
    min_score = score
    #최고 동일개수 구하기
    for i in range(len(lottos)):
        if lottos[i] == 0 and copy_cnt != 0:
            copy_cnt -= 1
            max_score += 1
    answer.append(max_score)
    
    #최저 동일개수 구하기
    #이 경우 0인 부분은 copy에 있는 숫자 제외 임의의 다른 숫자로 넣어 가정하면됨
    answer.append(min_score)
            
    
    
    
    #아직 answer에 담긴 최대, 최솟값은 아직 '일치개수'일 뿐이다.
    #로또 순위를 담아 리턴하자.
    end = []
    for num in answer:
        if num == 6:
            end.append(1)
        elif num == 5:
            end.append(2)
        elif num == 4:
            end.append(3)
        elif num == 3:
            end.append(4)
        elif num == 2:
            end.append(5)
        else:
            end.append(6)
            
    return end
    
