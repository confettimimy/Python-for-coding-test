import sys

n = int(sys.stdin.readline())
w = []
for _ in range(n):
    w.append(int(sys.stdin.readline()))

w.sort(reverse=True) # 30 25   20 15 10

weight = 0
possible=set() #로프들이 들 수 있는 최대중량
for k in range(1, n+1): # k개의 로프
    '''tmp = []
    for i in range(k):
        tmp.append(w[i])
    possible.add( tmp[-1] * k )'''
    # 위코드를 아래코드로 변형해 시간초과 해결 - k개 뽑은(가장 큰 순으로) 것 중 가장 작은 값만 가져오면 되니까!
    possible.add( w[k-1] * k )
    

#print(possible)
possible = list(possible)
print(max(possible))
     

#그리디 #정렬 
# 리스트, append 연산을 반복하면 시간이 꽤 늘어나는구나. .!를 알게된 문제 
