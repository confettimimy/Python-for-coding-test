''' Colletions 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공한다.
    리스트 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지 알려준다.
'''
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])


print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'이 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 변환
