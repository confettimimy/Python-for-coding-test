#sorted()나 sort()를 이용할 때에는 key 매개변수를 입력으로 받을 수 있다
#key값으로는 하나의 함수가 들어가야 하며 이는 정렬의 기준이 된다

#리스트의 데이터가 튜플로 구성되어 있을 때
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

#각 데이터의 두 번째 원소를 기준으로 설정
def setting(data):
  return data[1]


#정렬
result = sorted(array, key=setting) #key는 매개변수이며 key값으로는 함수가 들어가야 함
#출력
print(result)


#오류
'''result2 = array.sort()
print(result2,"zz")'''
