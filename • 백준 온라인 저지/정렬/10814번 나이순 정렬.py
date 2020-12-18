n = int(input())

arr = [ list(input().split()) for _ in range(n)]

for l in arr:
    l[0] = int(l[0])


# 회원을 나이 순, 나이가 같으면 가입한 순으로 정렬
arr.sort(key=lambda x: x[0])

for ls in arr:
       print(ls[0], ls[1])
