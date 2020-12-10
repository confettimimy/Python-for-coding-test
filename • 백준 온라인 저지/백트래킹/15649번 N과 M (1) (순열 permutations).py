from itertools import permutations


# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
n, m = map(int, input().split()) # (ex) 1~3 중에서 1개를 고른 수열

ls=[]
for i in range(1, n+1):
    ls.append(i)

for case in permutations(ls, m):
    #print(case)
    for number in case:
        print(number, end=' ')
    print('')
    



'''결국 여기서 쓰이진 않았지만 메모!
"".join(리스트) : join 함수는 리스트의 '문자열들'을 합치는 역할을 한다.
오류났던 이유 : join을 사용하는데 리스트 안의 요소들이 문자열이 아니라 숫자형이였어서. 주의하기!
'''
