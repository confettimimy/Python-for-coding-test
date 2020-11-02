def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            index = i
    
    answer = "김서방은 " + str(index) + "에 있다"
    return answer
