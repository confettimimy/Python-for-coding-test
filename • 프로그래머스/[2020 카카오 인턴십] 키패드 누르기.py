def solution(numbers, hand):
    answer = ''
    left_side = [1,4,7,'*']
    right_side = [3,6,9,'#']
    middle_side = [2,5,8,0]
    lnow = '*' #현재 왼손위치
    rnow = '#' #현재 오른손위치
    #arr = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    
    # 키패드 좌표료 변경
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    for i in range(0, len(numbers)):     
        if numbers[i] in left_side:
            answer += 'L'
        elif numbers[i] in right_side:
            answer += 'R'
        elif numbers[i] in middle_side:#[2,5,8,0]
            if abs(dic[numbers[i]][0]-dic[lnow][0]) + abs(dic[numbers[i]][1]-dic[lnow][1])  <  abs(dic[numbers[i]][0]-dic[rnow][0]) + abs(dic[numbers[i]][1]-dic[rnow][1]):
                answer += 'L'
            elif abs(dic[numbers[i]][0]-dic[lnow][0]) + abs(dic[numbers[i]][1]-dic[lnow][1])  >  abs(dic[numbers[i]][0]-dic[rnow][0]) + abs(dic[numbers[i]][1]-dic[rnow][1]):
                answer += 'R'
            elif abs(dic[numbers[i]][0]-dic[lnow][0]) + abs(dic[numbers[i]][1]-dic[lnow][1])  ==  abs(dic[numbers[i]][0]-dic[rnow][0]) + abs(dic[numbers[i]][1]-dic[rnow][1]):
                answer += hand[0].upper()
        
        #현재 왼손, 오른손 각각의 위치 기록
        if answer[-1]=='L':  #추가된 마지막 결과
            lnow = numbers[i]
        elif answer[-1]=='R':
            rnow = numbers[i]
        
        print(lnow, rnow,'check')

        
    return answer
