'''반례가 존재한다. 다른 방식으로 풀어보자. . .'''

n = int(input())
words = []
sett = set()
for _ in range(n):
    words.append( input() )
#print(words)

# 각 알파벳마다 n자리수 대로 우선순위 부여해 나중에 우선순위에 따라 정렬시키기
priority = [] # ['알파벳', 우선순위 수]
for word in words: # 'GCF' / 'ACDEB'
    i = len(word) #3
    score = 1 #1의자리수부터 시작 
    while True:
        if i==0:
            break
        priority.append( [word[i-1], score] )
        score += 1
        i-=1
    #한단어의 각 알파벳 마다의 우선순위 매기기 완료
#print(priority)



# 이제 우선순위에 따라 정렬시키기
priority.sort(reverse=True, key=lambda x:x[1])
#print(priority)



# 우선순위에 따라 정렬된 순서대로의 알파벳마다 9, 8, 7... 순서대로 부여
dic = dict()
k = 9
for j in range(len(priority)):
    if priority[j][0] not in dic.keys():
        dic[ priority[j][0] ] = k
        k -= 1
#print(dic)

#알파벳-숫자 상응시킨 뒤, 더하기 계산
l = []
for word in words: # 'GCF' / 'ACDEB'
    w = ''
    for c in word:
        w += str(dic[c])
    l.append(int(w))
#print(l)
print(sum(l))
