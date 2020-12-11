n = int(input())

table = []
for i in range(n):
    per_person = list(map(int, input().split()))
    table.append(per_person)


#print(table)


for i in table: # 한 명씩 가져와 순위(rank)를 출력시킨다.
    # 현재 i 사람을 기준으로!
    rank = 1
    
    # 전체를 순회하면서 i번째 사람보다 덩치가 큰 사람이 있는지 확인 (= '몸무게와 키 둘 다' 현재 i보다 커야 등수가 바뀔 수 있다.)
    for j in table:
        if i[0] < j[0] and i[1] < j[1]: # 현재 i보다 몸무게와 키 둘 다 능가하는 사람이 있다면
            rank += 1 # 현재 i의 등수가 내려간다.
            
    print(rank, end=' ')
