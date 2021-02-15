ls = list(map(int, input().split()))

# 1부터 8까지 숫자가 한 번씩 등장한다.

answer = ""

if ls == sorted(ls):
    answer = "ascending"
elif ls == sorted(ls, reverse=True):
    answer = "descending"
else:
    answer = "mixed"

print(answer)
