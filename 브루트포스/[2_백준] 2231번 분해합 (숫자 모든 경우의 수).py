n = int(input())


'''n = first + first[0] + first[1] + first[2]'''
count = n # 0 처리용

for first in range(n): # 가장 작은 값부터 시작한다, 어차피 가장 작은 생성자 찾는거니까, 브루트포스

    tmp_sum = 0
    for i in str(first):
        tmp_sum += int(i)

    if (first + tmp_sum) == n:
        print(first)
        break # 생성자 찾으면 바로 나옴 (생성자 중 최솟값만 구하면 되니까)

    count -= 1




# for문을 다 돌았는데 if문에 걸린 것이 하나도 없다면
# = for문을 break 없이 n번 다 돌았다면
# = 즉, 생성자가 하나도 존재하지 않는다면
if count == 0:
    print(0) # 0을 출력시킨다
