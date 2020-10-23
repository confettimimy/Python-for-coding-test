# 국영수 정렬 문제 -> 튜플로 구성된 리스트 정렬 기법을 사용해야 함
n = int(input()) #학생수

students = [] #학생 리스트
for i in range(n):
  input_data = tuple(input().split()) # 한 학생당 한줄씩 입력받고 튜플로 변환해서 저장
  students.append(input_data)


'''
[ 정렬 기준 ]
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
4) 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬
'''

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))


# 정렬된 학생 정보에서 이름만 출력
for student in students:
  print(student[0])
