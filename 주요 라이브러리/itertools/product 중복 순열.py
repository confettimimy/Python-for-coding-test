from itertools import product
# product 중복조합 : iterable객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우의 수
# 다만 원소를 중복하여 뽑는다
# 뽑고자 하는 데이터 수를 repeat 속성 값으로 넣어준다

data = ['A', 'B', 'C']

result = list( product(data, repeat=2) ) # 2개를 뽑는 모든 조합 구하기(중복 허용)

print(result)

'''출력 결과: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]'''
