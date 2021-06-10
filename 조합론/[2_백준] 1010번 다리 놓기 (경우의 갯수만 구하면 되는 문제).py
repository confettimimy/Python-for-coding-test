#from itertools import combinations
import math


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    '''
    ls = [0 for _ in range(m)]
    
    print(len(list(combinations(ls, n)))) # 어차피 경우의 수를 구하면 되는 문제인데 combinations( , )의 첫번째 인자가 iterable이여야 해서 m개 갯수만큼의 ls를 굳이 만들 필요는 없었다.
    '''

    # 여기서 시간을 줄일 수 있는 방법은 없을까?
    # 조합, 순열 라이브러리를 쓰면 항상 시간이 많이 걸린다

    # 결국 mCn 해서 갯수만 구하면 되는 문제 
    # nCr = n! / r!(n-r)!
    # mCn = ?
    # m! / n!*(m-n)!

    print( int(math.factorial(m)) // (int(math.factorial(n))*int(math.factorial(m-n))) )
