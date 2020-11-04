# 이중리스트 이용, for문으로 한 행씩 접근하여 품.
# 리스트 슬라이싱

# array배열 원본이 바뀌지 않도록 반드시 tmp_array배열 선언 필요
# 저번에 오류났던 이유가 다른건 다 같은 방식으로 풀었는데 tmp_array를 따로 선언하지 않고 array에 다시 넣었기 때문임. 즉, array 원본을 바꿔버려 다음 행의 연산에서 오류가 났기 때문.

def solution(array, commands):
    answer = []
    
    tmp_array = [] #과정 중 임시로 담아놓을 변수
    for i in range(len(commands)): #한 행마다 한 번씩 돌리기
        tmp_array = array[commands[i][0]-1 : commands[i][1]] #리스트도 문자열과 같이 슬라이싱이 가능함
        tmp_array.sort() #원본을 정렬된 상태로 바꿔버림
        print(tmp_array)
        answer.append( tmp_array[commands[i][2]-1] )
        
    return answer
    