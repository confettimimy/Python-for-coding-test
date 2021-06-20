# 메모리 초과 문제 ->
from itertools import permutations


t = int(input())

for _ in range(t):
    s = input()

    ls = []
    ls = list(permutations(s, len(s)))

    ls.sort()

    #print(ls)


    save_index = 0
    for i in range(len(ls)):
        if "".join(ls[i]) == s:
            save_index = i
        if save_index == len(ls)-1:
            save_index = i-1

    print("".join(ls[save_index + 1]))
