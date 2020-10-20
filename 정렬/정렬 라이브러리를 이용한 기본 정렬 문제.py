n = int(input())

array = []
for i in range(n):
  num = int(input())
  array.append(num)

array.sort()
array.reverse()

# 결과 출력
print(array) #이건 리스트 자료형으로 출력 ('[]'가 표시된다)
for i in array:
  print(i, end=' ')
