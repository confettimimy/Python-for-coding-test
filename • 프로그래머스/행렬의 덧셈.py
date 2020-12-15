# 이차원리스트 요소 변경 방식
def solution(arr1, arr2):
    answer = [[0]*len(arr1[0]) for _ in range(len(arr1))]
    # 0으로 초기화해주어야함. [0]이 아니라 [] 이렇게 빈 공간으로 냅두면 index out of range 에러가 난다.
    
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
            # 문자열 요소 변경은 불가하지만 숫자는 가능
    
    return answer



# numpy 라이브러리를 이용할 경우 까다로워져 이차리스트 요소 변경 방식으로 문제를 풀었다.
# (넘파이 형식 그대로 나오기 때문 / 컴마(,) 이런 것 일일히 다 찍어주어야 했기 때문)
# 하지만 tolist()를 이용하면 다음과 같이 풀이할 수 있다.
import numpy as np

def sumMatrix(A,B):
    A=np.array(A)
    B=np.array(B)
    answer=A+B
    return answer.tolist() ###

print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))
