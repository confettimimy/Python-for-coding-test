# 다량의 데이터 검색은 이진탐색 알고리즘을 이용해 효과적으로 처리할 수 있다.

# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array,target, start, end):
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


n = int(input())
array = list(map(int, input().split()))
array.sort() #이진탐색을 수행하기 위해 사전에 정렬 수행
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")

