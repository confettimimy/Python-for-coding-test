'''
bisect 라이브러리는 '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다. bisect라이브러리에서는 다음 아래 두 가지 함수가 가장 중요하게 사용된다.

bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
bisect_right(a, x): 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

'''
import bisect
 
sequence = [1, 3, 4, 5]
 
print(bisect.bisect(sequence, 2))
# bisect()는 a라는 오름차순으로 정렬된 시퀀스에 x값이 들어갈 위치를 리턴

'''-----------------------------------------------------------------'''

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]

print('4가 들어갈 위치 인덱스: ', bisect_left(a, 4))
print('6이 들어갈 위치 인덱스: ', bisect_right(a, 6))

