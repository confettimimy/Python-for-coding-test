from itertools import combinations

# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다.
arr = []
for i in range(9):
  arr.append(int(input()))


answer = []
for case in list(combinations(arr, 7)):
  sum = 0
  for i in case:
    sum += i
  if sum == 100: # [1] 이 부분을 바꿔 틀린 문제 해결 (for문 안에 넣었었다. 그렇게 하면 의미가 조금 달라짐)
    answer = sorted(list(case))
    break # [2]

# 결과출력
for j in answer:
  print(j)


''' <궁굼증>
[2] 가능한 정답이 여러 가지인 경우에는 아무거나 출력 ->
    순차탐색하며 가장 첫 번째로 나오는 걸로 출력하고 for문 나오기 (for 효율성)

    그렇게 했지만 break를 하든 안하든 똑같이 68ms가 걸렸다.
    완전탐색 브루트 포스 방식으로 풀었을 때 for문 중간에 break를 해서 나와도 시간효율성이 올라가지는 않는 것 같다.
    ---> 나중에 동적 프로그래밍?을 공부해 답이 나오면 뒤에는 실행하지 않는 파트 공부해보고 여기 궁굼증을 다시 해결하도록 하자. 
'''
