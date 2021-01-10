# 주어진 정렬된 수열에서 x가 등장하는 횟수를 출력하는 프로그램
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split())) # 오름차순으로 정렬되어 있는 수열 입력받기


if x not in arr:
    print(-1)
else:
    left_index = bisect_left(arr, x) # 정렬된 수열에서 x가 들어갈 위치 인덱스 출력 (왼쪽에서부터) (ex) 2
    right_index = bisect_right(arr, x) # (오른쪽에서부터) (ex) 6

    print(right_index - left_index)

# bisect는 이진 탐색 라이브러리이므로 문제 조건의 시간 복잡도에 걸리지 않을 것.
# 계속 오류났던 이유: bisect_right(arr, x)에서 ','을 '.'로 잘못쓴 실수가 있었음.
