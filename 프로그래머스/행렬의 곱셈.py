import numpy as np

def solution(arr1, arr2): 
    return np.dot( np.array(arr1), np.array(arr2) ).tolist()



''' NumPy : 다차원 배열 객체를 연산하는 도구 제공'''

#Array Creation
#numpy.array()함수로 생성

a = np.array([2,3,4])
print(a)
