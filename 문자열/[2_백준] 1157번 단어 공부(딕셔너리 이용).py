s = input().upper()

dic = {} #빈 딕셔너리 생성

# 문자열에서 문자 하나씩 꺼내며 어느 알파벳이 몇 번 등장했는지 딕셔너리에 기록한다.
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1 # 딕셔너리 쌍 추가

# 딕셔너리 현재 모습 확인
# print(dic)
# {'M': 1, 'I': 4, 'S': 4, 'P': 1}
# print(dic.items()) # items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.
# dict_items([('M', 1), ('I', 4), ('S', 4), ('P', 1)])

max_value = max(dic.values())

result = []
for key, value in dic.items():
    if value == max_value:
        result.append(key)

if len(result) == 1:
    print(result[0])
else:
    print('?')

    
