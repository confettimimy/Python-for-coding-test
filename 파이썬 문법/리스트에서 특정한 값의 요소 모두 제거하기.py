'''파이썬에서는 다른 프로그래밍 언어의 remove_all()과 같은 특정 값을 가지는 모든 원소를 제거하는 함수를 기본적으로 제공해주지 않으므로 다음과 같은 방법을 이용하면 좋다.'''

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만을 저장
result = []

for i in a:
    if i not in remove_set:
        result.append(i)

print(result)
