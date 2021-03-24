from itertools import permutations


n = int(input())

# 여기 처리 잊지말기!
ls = []
for i in range(1, n+1):
    ls.append(i)


all_case = sorted( list(permutations(ls, n)) )

for case in all_case:
    
    for factor in case:
        print(factor, end=' ')
    print()


