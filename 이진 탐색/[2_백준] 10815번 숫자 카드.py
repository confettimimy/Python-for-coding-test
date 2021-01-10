# <1920번 수 찾기> 문제와 거의 똑같은 문제 (수열의 개수만 다를 뿐)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target: # 왼쪽 다 잘라버리기
            start = mid + 1
        else:
            end = mid - 1
    return 0


n = int(input())
a = list(map(int, input().split()))
a.sort() # 이진탐색 수행 전 정렬돼 있어야함.

m = int(input())
num_to_find = list(map(int, input().split()))


for i in num_to_find:
    print(binary_search(a, i, 0, len(a)-1 ), end=' ')


