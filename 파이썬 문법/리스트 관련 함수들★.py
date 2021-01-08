a = [1, 4, 3]
print(a)


#리스트에 원소 삽입
a.append(2)
print(a)

#오름차순 정렬
a.sort()
print(a)

#내림차순 정렬
a.sort(reverse = True)
print(a)

#리스트 원소 뒤집기
a.reverse()
print(a)



#특정 인덱스에 데이터 추가
a.insert(2,3) #인덱스2에 값 3 추가
print(a)
'''+하지만 insert 남발 조심.. 시간복잡도로 테스트를 통과하지 못할 수도 있음.'''

#특정값 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

#특정값 데이터 삭제
a.remove(1) #값이 1인 데이터 삭제
print(a)

#특정값 데이터의 인덱스 위치 찾기
print("값이 4인 데이터의 인덱스 위치: ", a.index(4)) #배열 a에서 값이 4인 데이터의 인덱스 위치 반환


# 이 외에도.. 리스트 관련 함수에는 pop(), extend() 등이 있다.
