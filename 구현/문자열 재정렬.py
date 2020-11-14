s = input()

sum = 0
alphabet = [] # (문자열) 정렬을 사용해야하므로 리스트 이용

for c in s: # 문자열에서 문자 하나씩 꺼내서
    if c.isalpha(): #알파벳이면
        alphabet.append(c)
    else: #숫자이면
        sum += int(c)

alphabet.sort() #문자도 정렬라이브러리를 이용해 정렬 가능, 현재 리스트 형태.

# [1]
for i in alphabet:
    print(i, end='')
print(sum, end='')

print('')
# [2] 다음과 같이 출력하는 방식도 권장
if sum != 0: #이와 같은 처리도 해주자, 0일 경우 뒤에 0이 붙여지면 오류가 날 것임
    alphabet.append(str(sum))

print(''.join(alphabet))
