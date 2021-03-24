from itertools import permutations


n, m = map(int, input().split())

arr = list(map(int, input().split()))

all_case = sorted(list(permutations(arr, m)))

for case in all_case:
    for c in case:
        print(c, end=' ')
    print()
