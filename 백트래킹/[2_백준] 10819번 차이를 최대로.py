# 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

# N (3 ≤ N ≤ 8) -> n의 수가 크지 않다.

answer = 0
for case in permutations(arr, n):
    #print(case)
    case = list(case)
    sum = 0
    for i in range(n-1):
        sum += abs(case[i] - case[i+1])

    if sum > answer:
        answer = sum

print(answer)

