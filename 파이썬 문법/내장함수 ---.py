'''eval() 함수는 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.
   참고로 "012" 같이 앞에 0이 들어오는 것은 계산 불가능'''
result = eval("(3 + 5) * 7")
print(result)


result = sum([1, 2, 3, 4, 5])
print(result)


result = min(7, 3, 5, 2)
print(result)


result = max([7, 3, 5, 2])
print(result)
