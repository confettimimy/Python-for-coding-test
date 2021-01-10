# 이진탐색: 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 알고리즘
# 다량의 데이터 검색 문제에서는 이진탐색 알고리즘을 통해 효과적으로 처리가능
# 이진탐색은 배열이 정렬돼 있어야만 사용할 수 있다
# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print('찾고자 하는 값은 배열의 ', result + 1, '번 째에 있습니다.')
