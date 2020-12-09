from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))


# M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
tmp_sum = 0
tmp_list = []
for case in combinations(cards, 3):
    tmp_sum = case[0] + case[1] + case[2]
    if tmp_sum <= m:
        tmp_list.append(tmp_sum)

print(max(tmp_list))
