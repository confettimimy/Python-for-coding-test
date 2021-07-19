from itertools import combinations
import sys

answer = 0


n = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))

ls = set()
for i in range(1, len(S)+1):
    for case in list(combinations(S, i)):
        ls.add( sum(list(case)) )
#print(ls)

ls = sorted( list(ls) )
#print(ls)

for k in range(0, len(ls)):
    if ls[k] != (k+1):
        answer = k+1
        break
if answer == 0:
    answer = ls[-1]+1
print(answer)

'''시간초과도 여러번 났던 문제
sort 정렬시켜서 맨앞 숫자부터 탐색해 찾는 즉시 바로 break함으로써 시간을 단축시켜 해결되지 않았나 싶음.
다 탐색해도 여전히 answer이 0이라면의 예외처리까지 완벽하게 처리.
'''
