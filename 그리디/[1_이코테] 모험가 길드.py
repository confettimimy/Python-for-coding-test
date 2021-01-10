# 공포도가 낮은 모험가부터 묶기 시작해야 그룹수를 늘리기 좋다.
# -> 공포도를 오름차순으로 정렬하면, 항상 최소한의 모험가의 수만 포함하여 그룹을 결성할 수 있다.

n = int(input())
horrors = list(map(int, input().split()))

horrors.sort()
# [1 / 2, 2 / 2, 3]

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for h in horrors: # 공포도가 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기

    if count >= h: # '공포도가 X인 모험가는 반드시 X명 이상으로 구성한 그룹에 넣어야 한다.'
        result += 1 # 그룹 결성
        count = 0 # 현재 그룹의 모험가 수 초기화

print(result) # 총 그룹의 수 출력

