# 백준 1743번 음식물 피하기 문제 참고


x = 10
 
def func():
    global x 
    x += 1
    
    print(x)
 
func()



'''UnboundLocalError: local variable 'x' referenced before assignment 오류

전역 변수를 지역 범위에서 사용하고 싶다면 지역 영역에서 global키워드를 사용한다.
이렇게 하면 지역 범위에서 전역 변수를 사용할 수 있게 된다.

'''
