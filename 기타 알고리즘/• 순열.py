import itertools

data = [1, 2]

for x in itertools.permutations(data, 2):
    print(x, end=' ')
# (1, 2) (2, 1) 

print()

for x in itertools.permutations(data, 2):
    print(list(x), end=' ')
# [1, 2] [2, 1]

