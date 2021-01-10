n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))


sum = 0
for _ in range(n):
    sum += (max(B) * min(A))
    B.remove(max(B))
    A.remove(min(A))

print(sum)

'''+ 본인은 '정렬'개념을 이용해서 풀진 않았다.

   A를 sort(), B를 sort(reverse=True)로 해서 같은 인덱스 위치에 있는 값끼리 곱해서 최솟값을 출력해도 된다.
   B배열 요소들을 다시 원래대로 재배열 해놓을 필요가 없다. 그냥 최솟값만 출력하면 되기 때문.
'''
