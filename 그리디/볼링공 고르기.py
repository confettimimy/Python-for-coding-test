from itertools import combinations

n, m = map(int, input().split()) # 볼링공 개수 N, 각 볼링공의 무게는 1~M까지 존재
arr = list(map(int, input().split())) # 볼링공 각각의 무게가 들어있는 리스트 arr
# 1 3 2 3 2

count = 0


# 두 사람은 서로 무게가 다른 볼링공을 골라야 한다.
# 또한 같은 무게의 공이 여러 개 있을 수 있지만 서로 다른 공으로 간주한다.

'''
for i in arr: #1

    for j in arr: #1,3,2,3,2
        if i==j: # 서로 무게가 같다면 제외 => 자기 자신을 또 넣는 것도 방지!
            pass
        else: # 서로 무게가 다르면 조합가능
            count += 1
print(count)

# 하지만 이 방식으로 접근하면 이미 계산했던 경우까지 중복하여 count+=1을 하기 때문에 틀린 결과가 나옴.
# 즉 예를 들어 (1, 2) (2, 1) 이 경우 서로의 무게가 다르긴 하지만 같은 경우인데 다른 경우로 묶어버려서 안된다.
# 따라서 (1, 2)와 (2, 1)을 같은 경우로 취급하는 '조합' 개념을 이용해야 한다.
'''



for case in combinations(arr, 2):
    if case[0] == case[1]: # 서로의 볼링공 무게가 똑같다면
        pass
    else:
        count += 1
# 조합 개념이니 알아서 서로 다른 '원소'를 골랐을 것

print(count)

