from collections import Counter

n = int(input())
ls = []
for _ in range(n):
    ls.append(input())

dic = dict(Counter(ls))
#print(dic)

ls = [] # 가장 많은 수를 찾으려고 수대로 정렬을 할건데 딕셔너리 자료형은 sort()를 지원하지 않으니 자체적으로 리스트 자료형으로 바꾼다.
for title in dic.keys():
    ls.append([title, dic[title]])
#print(ls)


'''가장 많이 팔린 책의 제목을 출력한다. 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.'''
'''ls.sort(key=lambda x:(x[1], -x[0]), reverse=True)
   -> TypeError: bad operand type for unary -: 'str' 오류가 난다.
   그럼 반대로 전환해 생각해보자. 아래 코드 check'''
ls.sort(key=lambda x:(-x[1], x[0]))
#print(ls)


print(ls[0][0])


'''해시 + 정렬 문제
- 해시를 이용해(=> Counter이용) 개수를 세서 가장 많은 수인 것을 출력.
- sort()를 이용하려면 딕셔너리-> 리스트 자료형으로의 변환 작업 필요
- 정렬시 중요. -x[0] 이렇게 -를 붙이려면 문자열 형태엔 적용 불가능하고 숫자인 경우에만 가능, 역발상을 활용해보자'''
