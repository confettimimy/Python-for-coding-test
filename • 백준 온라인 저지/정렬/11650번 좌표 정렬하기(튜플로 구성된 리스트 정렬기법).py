n = int(input())

array = []
for _ in range(n):
    array.append( tuple(map(int, input().split())) )

# 튜플 원소로 구성된 리스트 정렬 기법을 사용해야함

'''array.sort(key=lambda x: x[0] ) # 이 경우 x[0] 기준으로만 정렬됨. 첫 번째 요소가 같은 경우 두 번째 원소 기준으로 또 정렬시키려면.. 아래와 같이 한다.'''
array.sort(key=lambda x: (x[0], x[1]) ) #x가 같으면 y좌표가 증가하는 순서대로 정렬하기

for a in array:
    print(a[0], a[1])
#틀렸던 이유: 현재 상태는 튜플 상태. 튜플 자료형으로 반환하는 것이 아니었다.
