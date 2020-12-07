'''암호는 서로 다른 l개의 알파벳 소문자들로 구성되며,
   최소 한 개의 모음과 최소 두 개의 자음으로 구성되어 있다. <- 이 문제조건을 간과했음.'''

from itertools import combinations


# 5개의 모음 정의
vowels = ('a', 'e', 'i', 'o', 'u')

l, c = map(int, input().split()) # 암호는 서로 다른 l개의 알파벳 소문자로 구성된다.
char_type = input().split() # 암호로 사용했을 법한 문자의 종류


result = []

for case in combinations(char_type, l):
    
    vowel_cnt = 0 ### [1]
    not_vowel_cnt = 0
    
    for c in case:
        if c in vowels:
            vowel_cnt += 1
        else:
            not_vowel_cnt += 1
            
    if vowel_cnt >= 1 and not_vowel_cnt >= 2:
        #print(vowel_cnt, not_vowel_cnt) # 확인용 ### [1]
        result.append(''.join(sorted(case)))



result.sort()
for r in result:
    print(r)

'''[1]
   모음, 자음 개수를 각각출력시켜보니 틀린 원인을 알게 됐다. vowel_cnt, not_ vowel_cnt 이 변수들을 다시 0으로 세팅해주지 않아 원하는 모습이 나오지 않던 것이였다.'''
