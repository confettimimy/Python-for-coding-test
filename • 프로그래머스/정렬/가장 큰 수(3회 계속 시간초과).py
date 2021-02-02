from itertools import permutations

def solution(numbers):
    ls = []
    
    for case in permutations(numbers, len(numbers)):
        #print(case)
        
        num=''
        for a in case:
            num += str(a)
        ls.append(int(num))
    
    #print(ls)
    return str(max(ls))
