from itertools import combinations
# combinations 조합 : iterable객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산 (순서 상관 X)

data = ['A', 'B', 'C']

result = list( combinations(data, 2) ) # 2개를 뽑는 모든 조합 구하기

print(result)

'''출력 결과: [('A', 'B'), ('A', 'C'), ('B', 'C')]'''