n = input()
num = len(n) #입력받은 문자열의 개수

before = 0
after = 0

for i in range(num//2):
    before += int(n[i]) #문자열 인덱싱 이용
for j in range(num//2, num):
    after += int(n[j])

if before == after:
    print("LUCKY")
else:
    print("READY")


