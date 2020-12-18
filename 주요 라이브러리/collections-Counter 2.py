import collections

lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']

print(collections.Counter(lst))

# 실행 결과: Counter({'aa': 2, 'cc': 1, 'dd': 1, 'bb': 1, 'ee': 1})


''' - collections에 내장된 함수인 Counter()는 Dic과 같이 hash형 자료들의 값의 개수를 셀 때 사용
    - Dic처럼 {key:value} 형식으로 만들어짐
    - Counter() 객체끼리 빼는 것도 가능
    - 해당하는 값이 없더라도 error가 아닌 0을 반환
'''