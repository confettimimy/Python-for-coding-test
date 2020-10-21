# 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수 찾기
# 공백으로 구분하여 입력받기
# min(), max()함수 이용 - 값으로 리스트 넣기 가능

n, m = map(int, input().split())

array = [] #행마다 가장 작은 값 저장해두는 리스트

for i in range(n): #한 행씩 값 입력받기
    input_line = list( map(int, input().split()) ) #input_line은 리스트
    array.append( min(input_line) )

result = max(array) #각 행마다 뽑은 가장 작은 값들의 배열 중 가장 큰 값 고르기
print(result)

# 굳이 이중포문을 이용해 입력받지 않아도 됨, 한 줄씩 입력 받기 가능
