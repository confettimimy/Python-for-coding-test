import math

n, m = map(int, input().split(':'))

gcd = math.gcd(n, m)

print(str(int(n/gcd)) + ':' + str(int(m/gcd)))
