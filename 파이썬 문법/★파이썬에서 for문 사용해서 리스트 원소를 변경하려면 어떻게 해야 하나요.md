## 파이썬에서 for문 사용해서 리스트 원소를 변경하려면 어떻게 해야 하나요?



파이썬에서 리스트 내의 원소중에 조건을 만족하는 원소는 다른 값으로 변경하려고 합니다.

   

```python
temp = ['apple', 'banana', 'coke']

for one in temp:
    if one == 'coke':
        one = 'grape'

print(temp)
```

이렇게 할 경우에 ['apple', 'banana', 'grape'] 가 될거라고 생각했는데 안 된다.

```python
temp = ['apple', 'banana', 'coke']
i = 0

for temp[i] in range(len(temp)):
    if temp[i] == 'coke':
        temp[i] = 'grape'

print(temp)
```

이렇게 하면 문제 없다.

   

### 아래처럼 해야하는 이유

이 코드 중 `for one in temp`를 보자구요! `one`로 `temp`의 원소를 하나씩 **복사**해 넣는 줄이네요. 다시 말해, 주소(객체)가 전달된 것이 아니고 **값 만이 복사되어 전달된 것**이므로, 이 방법으로는 값을 변경할 수 없다는 결론이 나와요.

   

### [출처](https://hashcode.co.kr/questions/8870/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-for%EB%AC%B8-%EC%82%AC%EC%9A%A9%ED%95%B4%EC%84%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%9B%90%EC%86%8C%EB%A5%BC-%EB%B3%80%EA%B2%BD%ED%95%98%EB%A0%A4%EB%A9%B4-%EC%96%B4%EB%96%BB%EA%B2%8C-%ED%95%B4%EC%95%BC-%ED%95%98%EB%82%98%EC%9A%94)

여지껏 긴가민가 했던 부분 확실하게 해결