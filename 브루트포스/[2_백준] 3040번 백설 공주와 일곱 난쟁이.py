from itertools import combinations

ls = []
for _ in range(9):
    ls.append(int(input()))


for case in combinations(ls, 7):
    case = list(case)

    if sum(case) == 100:
        for nanjange in case:
            print(nanjange)
            
