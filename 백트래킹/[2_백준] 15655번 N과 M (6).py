from itertools import combinations


n, m = map(int, input().split())

ls = list(map(int, input().split()))


# 첫 번째, 요소 내의 정렬
tuple_sorted = []
for case in list(combinations(ls, m)):
    tuple_sorted.append( sorted(list(case)) )

'''print(tuple_sorted)'''


# 두 번째, 전체 정렬
all_sorted = sorted(tuple_sorted)



for one in all_sorted:
    for o in one:
        print(o, end=' ')
    print()
