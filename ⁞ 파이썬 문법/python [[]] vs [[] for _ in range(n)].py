array1 = [[]] * 10
array1[0] = 0
print(array1)


array2 = [[] for _ in range(10)]
array2[0] = 0
print(array2)


# 두 방식 모두 [0, [], [], [], [], [], [], [], [], []]이 출력됨
