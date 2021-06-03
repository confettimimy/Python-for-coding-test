from itertools import combinations # 순서 따지지 않는다. 순열 필요x




# 사용자 입력받기
k = 0
while True:
    input_ls = list(map(int, input().split()))

    k = input_ls[0]
    input_ls = input_ls[1:]

    if k == 0:
        break



    for case in list(combinations(input_ls, 6)): # k개는 S집합의 개수일 뿐이고, 독일로또는 k개를 뽑는게 아니라 6개를 뽑는 것이라고 문제 조건에 명시돼있었다.
        for o in case:
            print(o, end=' ')
        print()
    print('')
