# 데이터의 개수 입력
n = int(input())


#각 데이터를 공백으로 구분하여 입력
#숫자 데이터로 구성된 리스트 형태로  반환
data = list(map(int, input().split()))

data.sort()
print(data)



# n,m,k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())
print(n,m,k)
