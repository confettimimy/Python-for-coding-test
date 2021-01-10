n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# n개의 배열 원소, 최대 k번 바꿔치기 가능

a.sort() #작은 순으로 정렬
b.sort(reverse=True) #큰 순으로 정렬
print(a, ' a배열 리스트의 정렬 모습')
print(b, ' b배열 리스트의 정렬 모습')

for i in range(k): #k번 배열 원소 교체하기
  a[i] = b[i]

sum = 0

for j in range(n):
  sum += a[j]

print(sum)
