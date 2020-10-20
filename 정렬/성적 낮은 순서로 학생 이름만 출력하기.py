# 학생수 입력받기
n = int(input())

array = []

for i in range(n):
  input_data = input().split() #split은 리스트 형태로 반환
  # 현재 input_data는 리스트의 모습
  array.append( (input_data[0], int(input_data[1])) )#리스트 데이터에 인덱싱으로 접근

def setting(data): #리스트로 들어오면 값으로 내보낸다
  return data[1] #성적 숫자를 정렬의 기준값으로 잡는다

result = sorted(array, key=setting) #성적이 낮은 순서대로 = 오름차순

#확인을 위해 리스트 형태로 일단 출력
print('정렬된 현재 리스트의 모습 확인: ', result) 



#성적이 낮은 학생대로 이름만을 출력한다
'''튜플데이터로 구성된 리스트에서 어떻게 튜플 특정 인덱스만 출력하지?
   --> 튜플도 리스트 자료형처럼 인덱싱으로 접근 가능!!! 이중배열처럼 생각하기!'''
print(result[0][0])
print(result[1][0])

for i in range(n): #배열이름, 아니면 range()꼭 붙여서 숫자변수!
  print(result[i][0], end=' ')
