# 문제조건의 탐색범위가 넓다 -> 이진탐색 사용하기 (브루트포스 방식으로 했다가 시간초과났음.)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if target == array[mid]:
            return 1
        elif target > array[mid]: # 왼쪽 다 잘라버리기
            start = mid + 1
        else:
            end = mid - 1
    return 0



n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
num_to_find = list(map(int, input().split()))
# [틀림 해결] num_to_find.sort() # 여기는 정렬시키면 안됨. 아래 포문에서 순서대로 출력시켜야 함.


for i in num_to_find:
    print(binary_search(a, i, 0, len(a)-1))

