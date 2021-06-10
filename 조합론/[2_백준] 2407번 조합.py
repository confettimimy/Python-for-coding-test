import math


n, m = map(int, input().split())

# nCm = n! / (n-m)!m!
print( math.factorial(n) // (math.factorial(n-m)*math.factorial(m)) )
