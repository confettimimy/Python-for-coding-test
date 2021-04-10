from itertools import combinations # 순서상관x, 중복불가

m = int(input()) # 색상 종류 개수
per_color_cnt = list(map(int, input().split())) # 각 색상의 조약돌이 몇 개 있는지
k = int(input()) # k개 뽑는다


# combinations( , )의 전자 부분에 넣을 인자로, iterable 리스트를 생성한다
ls = []
for i in range(m):
    for j in range(per_color_cnt[i]):
        ls.append(i)
#print(ls) #확인





# 모든 경우의 수 구하기
all_case = len(list(combinations(ls, k)))





# 분자에 넣을 수 구하기
sample_case = 0

tmp_index = 0
for p in range(m):
    sample_case += len(  list(combinations(ls[tmp_index : tmp_index + per_color_cnt[p]], k)) ) # tmp_index + per_color_cnt[p]] 여기에서 'tmp_index +'를 안해줘서 틀렸던 거임.
    tmp_index = per_color_cnt[p]





# 확률 출력
print(sample_case/all_case)


'''<메모리 초과 문제>
https://mimimimamimimo.tistory.com/5
이 분꺼 참고하고 해결하기
'''
