# 리스트 컴프리헨션은 2차원 리스트를 초기화할 때 매우 효과적으로 사용될 수 있다.
# N x M 크기의 2차원 리스트를 초기화할 때는 다음과 같이 사용한다.

n = 3
m = 4
array = [[0] * m for _ in range(n)]

print(array)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
