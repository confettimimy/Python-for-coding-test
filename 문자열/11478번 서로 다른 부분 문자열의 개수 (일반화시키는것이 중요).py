s = input()

possible = set()
for k in range(1, len(s)+1): # 1~5
    
    # k=2, n=1
    n=0
    for i in range(0, len(s)-n):
        possible.add( s[i:i+k] )
    n+=1

#print(possible)
print(len(list(possible)))


'''후기
1. 일반화시키는 것이 중요
2. s[i:i+k] 문자열 접근방식 (처음에는 이같이 안했다. 코드만 길어지고 난잡해지면서 길잃고..)
'''
