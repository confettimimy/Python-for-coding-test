# n시 59분 59초까지 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력하기
# i   / j    / k
# 0~n / 0~59 / 0~59

h = int(input())

count = 0 #모든 경우의 수

for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k): #3이 하나라도 포함되는 모든 경우
        count+=1 


print(count)
