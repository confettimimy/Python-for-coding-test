import sys

n = int(input()) #기록수

now = {} # [1]
for _ in range(n):
    history = sys.stdin.readline().split() # [2]
    # ['Baha', 'enter']
    # print(history)

    if history[1] == 'enter':
        now[history[0]] = True # [1]
    elif history[1] == 'leave':
        del now[history[0]] # [3]


#now.sort(key=lambda x: x[0], reverse = True) #AttributeError: 'dict' object has no attribute 'sort'
ls = []
ls = list(now.keys())
ls.sort(reverse = True)
for one in ls:
    print(one)


'''<시간초과 오류>
로그에 기록된 출입 기록의 수 n이 주어진다. (2 ≤ n ≤ 106)

1. Dictionary를 이용하여 데이터를 저장 -> 시간효율성 굿.
2. 속도 향상을 위해, 콘솔 입력을 sys.stdin.readline() 사용 - 많은 양을 입력받을때 효율성을 위해 꼭쓰자!
3. 메모리 최소화 및 속도향상을 위해 leave(퇴근)인 경우 del로 메모리 해제


즉, 리스트 자료형을 사용해 append(), remove() 이런 식으로 했을 때는 시간초과 문제 발생.
많은 양의 데이터 입력을 위해 [2]방식을 사용했고, 많은 양의 탐색이기 때문에 딕셔너리 자료형으로 바꿔(True는 사실 의미없는 값인데 딕셔너리 자료형을 사용하는 것 자체만으로 시간효율이 엄청나게 올라간다)
시간초과 문제를 해결했다!

'''
