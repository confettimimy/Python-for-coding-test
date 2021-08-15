from itertools import permutations
import sys

n = int(sys.stdin.readline())
target = tuple(map(int, sys.stdin.readline().split()))

ls = [i for i in range(1, n+1)]


arr = list(permutations(ls, n))
#print(arr)
for i in range(len(arr)):
    if i==0 and target==arr[i]:
        print(-1)
        break
    elif arr[i] == target:
        for p in arr[i-1]:
            print(p, end=' ')
        break #여기 들여쓰기가 문제였구만 !
'''i 해당 조건에 맞는 것을 찾으면
   그 이전의 i-1을 출력시켜야하기 때문에
   for i in range():
      i, i-1
   를 사용하는 것이 적절 
'''

'''정답은 맞지만 메모리초과
   메모리초과 문제를 해결하려 sort()도 빼고, 정답 보이면 바로 끝내려고 코드도 더 효율적으로 바꿔보았지만 해결하지 못했다.
   다른 언어의 경우 통과된다고 한다. . .파이썬으로 푼 다른 분의 코드도 역시 똑같이 메모리초과가 떴다.
   파이썬 언어가 극도로 느린 만큼, pypy로 제출해도 메모리초과. 언어의 한계인 것 같다. 다른 언어로 풀어야 해결가능할듯 
'''
