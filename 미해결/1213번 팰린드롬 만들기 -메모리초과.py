from itertools import permutations
#알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.


s = input()

possible=set()
for case in list(permutations(s, len(s))):
    #word = "".join(case) #문자열 상태
    print(case)
    print(case[::-1])

    if case == case[::-1]: #"".join(list(reversed(list(word)))): #메모리초과로 슬라이싱 기법 이용한 뒤집기 시도했지만 여전히 메모리초과.
        case = "".join(case)
        possible.add(case)


if len(possible)==0:
    print("I'm Sorry Hansoo")
else:
    new = sorted(list(possible))
    for one in new:
        print(one)

