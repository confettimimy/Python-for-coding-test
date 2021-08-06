**2차원 이상의 다차원 리스트는 리스트를 완전히 복사하려면 copy 메서드 대신 copy 모듈의 deepcopy 함수를 사용해야 합니다.**

```python
>>> a = [[10, 20], [30, 40]]

>>> import copy             # copy 모듈을 가져옴
>>> b = copy.deepcopy(a)    # copy.deepcopy 함수를 사용하여 깊은 복사

>>> b[0][0] = 500

>>> a
[[10, 20], [30, 40]]
>>> b
[[500, 20], [30, 40]]
```

​    

[출처](https://dojang.io/mod/page/view.php?id=2294)