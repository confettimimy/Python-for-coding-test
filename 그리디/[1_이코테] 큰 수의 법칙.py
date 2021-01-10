#  주어진 수들을 m번 더하여, 특정 값을 '연속해서' k번까지만 더할 수 있음
n, m, k = map(int, input().split())

data = list(map(int, input().split())) #n개의 자연수 입력

# max(data) #관련 내장함수 형태가 생각이 안나서 막혔었다.

data.sort()
print(data)
first = data[-1] #가장 큰 수
second =  data[-2] #두 번째로 큰 수

result = 0 #결과값
count = k #k는 리밋 설정값으로 초기화 돼있음

for i in range(m): #총 m번 더한다
  if count == 0:
    result += second #한번만 더한 후,
    count = k #다시 리밋 설정값으로 초기화해준다
    print(result) #결과값 확인
    continue ### 아래 코드를 실행하지 않고 건너뜀
  
  result += first
  count -= 1
  print(result) #결과값 확인


print('큰 수의 법칙에 따른 결과값: ', result)
# 알고리즘을 맞게 짠 것 같은데 왜 결과가 다르게 나올까?
# if문에서 break를 안해주니까 first, second 값을 모두 더하게돼서 결과값이 다르게 나옴. 
# 다시 오류 -> for문 전체 말고 if문만 나오게 하는 방법은? (포스텍 과제에서도 걸렸던 문제) break를 하니까 for문을 아예 다 빠져나와버림
# break가 아닌 continue를 하면 됨.
