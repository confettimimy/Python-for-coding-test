from itertools import permutations
# permutations 순열 : iterable객체에서 r개의 데이터를 뽑아 일렬로 나열 (순서 고려 O)

data = ['A', 'B', 'C']

result = list( permutations(data, 3) ) # 모든 순열 구하기

print(result)

'''출력 결과: [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]