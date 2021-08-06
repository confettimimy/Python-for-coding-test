[파이썬 내장함수 참고](https://docs.python.org/ko/3/library/functions.html)

[for문 사용해서 리스트 배열의 원본값을 변경하려면](https://github.com/confettimimy/Python-for-coding-test/blob/master/%ED%8C%8C%EC%9D%B4%EC%8D%AC%20%EB%AC%B8%EB%B2%95/%E2%98%85for%EB%AC%B8%20%EC%82%AC%EC%9A%A9%ED%95%B4%EC%84%9C%20%EB%A6%AC%EC%8A%A4%ED%8A%B8%20%EC%9B%90%EC%86%8C%EB%A5%BC%20%EB%B3%80%EA%B2%BD%ED%95%98%EB%A0%A4%EB%A9%B4%20%EC%96%B4%EB%96%BB%EA%B2%8C%20%ED%95%B4%EC%95%BC%20%ED%95%98%EB%82%98%EC%9A%94.md)

[파이썬 리스트 값 수정, 제거(del, remove, pop)](https://hogni.tistory.com/47) 

ㄴ<값 수정의 경우> 리스트(mutable한 자료형이라)값 수정은 가능하며 문자열(immutable해서)의 경우는 이런 식으로 값 변경불가

[거꾸로 s.reverse() / reversed(s) / s[::-1] ](https://itholic.github.io/python-reverse-string/)

​    

[리스트 복사 - 깊은복사, 얕은복사](https://hcr3066.tistory.com/74)

1. list()를 이용해 복사한다.

2. 2차원 이상의 다차원 리스트는 리스트를 완전히 복사하려면 copy 메서드 대신 copy 모듈의 deepcopy 함수를 사용해야 한다. (이는 파이썬 문법 폴더에 설명)

   ```python
   from copy import deepcopy
   a= [[1,2],[3]]
   b= deepcopy(a)
   ```

​    

