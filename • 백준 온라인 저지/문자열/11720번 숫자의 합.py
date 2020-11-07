n = int(input())

#둘째 줄에 숫자 N개가 '공백없이' 주어진다 -> 문자열로 받는다
numbers = input()

sum = 0
for i in numbers: 
    sum += int(i)

print(sum)

