import math
from collections import Counter

n = int(input())

count=0
m = str(math.factorial(n))
m = list(reversed(m))
#print(m)
for c in m:
    if c != '0':
        break
    count+=1

print(count)
        

