# continue, break 차이 확실히 알고가기

for i in range(10):
  if i == 5:
    print('wow')
    continue ### 아래 코드를 실행하지 않고 건너뜀
  
  print('continue 아래 코드')

# if문에서 break를 써버리면 for문 전체를 빠져나와버림
# continue를 쓰면 해당 아래코드를 건너뛰고 다시 루프문에 들게 할 수 있다.


'''continue는 반복문에서 사용된다.
   [case1] for문에서 continue로 코드 실행 건너뛰기
   [case2] while 반복문에서 continue로 코드 실행 건너뛰기
# 
