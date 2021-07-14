def solution(s):
    answer = ''
    tmp_word = ''
    
    dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    for c in s:  
        if c.isdigit():
            answer += c
        else: #문자라면
            tmp_word += c
            
        if tmp_word in dic.keys():
            #print(tmp_word,'그순간 출력')
            answer += str( dic[tmp_word] )
            tmp_word = '' #다시 초기화
    
    #print(answer)
    return int(answer)
