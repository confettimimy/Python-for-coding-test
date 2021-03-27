import sys # 빠르게 입력받기로 시간초과 문제 해결!


n = int(sys.stdin.readline())

A = [] # 에상 등수
for _ in range(n):
    A.append(int(sys.stdin.readline()))

B = [i for i in range(1, n+1)] # 실제 등수


A.sort()


upset_sum = 0
for k in range(n):
    upset_sum += abs(A[k] - B[k])

print(upset_sum)
