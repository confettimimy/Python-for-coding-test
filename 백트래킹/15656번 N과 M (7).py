from itertools import product #combinations_with_replacement - 예제 출력결과 보니까 순서가 중요함 

n, m = map(int, input().split())
ls = list(map(int, input().split()))

ls.sort()

for case in list(product(ls, repeat=m)):
    for one in case:
        print(one, end=' ')
    print()
