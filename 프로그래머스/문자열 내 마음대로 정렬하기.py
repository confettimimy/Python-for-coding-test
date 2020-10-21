def solution(strings, n):
    answer = []
    
    arr=[]
    for string in strings:
        arr.append(string[n]+string) #idea
    
    arr.sort() 
    # 문자열도 오름차순으로 정렬이 가능
    # 'a'문자 하나만 되는게 아니라, 단어구일때도 맨 앞 문자 기준으로 정렬이 됨!
    print(arr)
    
    for k in range(len(arr)):
        answer.append(arr[k][1:]) #idea
    
    
    return answer
