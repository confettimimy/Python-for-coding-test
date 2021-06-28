from itertools import combinations_with_replacement
# 순서는 신경쓰지 않아도 되지만, 중복 선택 가능 = 중복조합 


n = int(input())

#roma = {'I':1, 'V':5, 'X':10, 'L':50}
ls = [1, 5, 10, 50]
possible = []

for case in list(combinations_with_replacement(ls, n)):
    #print(case)
    sum = 0
    for k in case:
        sum += k
    if sum not in possible:
        possible.append(sum)

#print(possible)
print(len(possible))
