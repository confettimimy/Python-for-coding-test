def solution(n, arr1, arr2):
    answer = []
    
    arr1_new = []
    arr2_new = []
    
    
    for a in arr1:
        arr1_new.append( str(bin(a))[2:] )
        if len(arr1_new[-1]) != n:
            adder = '0' * (n-len(arr1_new[-1])) 
            arr1_new[-1] = adder + arr1_new[-1]
    for b in arr2:
        arr2_new.append( str(bin(b))[2:] )
        if len(arr2_new[-1]) != n:
            adder = '0' * (n-len(arr2_new[-1]))   
            arr2_new[-1] = adder + arr2_new[-1]
    
    
    print(arr1_new)
    print(arr2_new,'확인')
    
    
    one_line = ""
    for i in range(n):
    
        for a, b in list(zip(arr1_new[i], arr2_new[i])):
            if int(a) | int(b) == True:
                one_line += "#"
            else:
                one_line += " "
                
        answer.append(one_line)
        one_line = "" #초기화 까먹지 않기!
        
        
        
    return answer
