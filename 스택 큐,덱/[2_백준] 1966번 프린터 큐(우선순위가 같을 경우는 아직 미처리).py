t =  int(input())


for _ in range(t):
    array = [] # 딕셔너리형의 역할을 할 리스트
    n, m = map(int, input().split())
    priority = list(map(int, input().split())) # 각 문서마다 중요도


    for i in range(n):
        array.append((i, priority[i]))

    print(array)

    array.sort(key=lambda x: x[1], reverse=True)

    print(array)

    for a in array:
        if m == a[0]:
            print('위치', array.index(a)+1)
