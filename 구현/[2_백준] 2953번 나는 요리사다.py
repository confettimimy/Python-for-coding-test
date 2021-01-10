scores = []
for _ in range(5):
    scores.append(sum(list(map(int, input().split()))))

print(scores.index(max(scores))+1, max(scores))
# 항상 우승자가 유일한 경우만 입력으로 주어진다.
 
