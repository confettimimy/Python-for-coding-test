from itertools import permutations


t = int(input())

for _ in range(t):
    
    n = int(input()) #지원자의 수

    ls = []
    for k in range(n):
        one, two = map(int, input().split())
        ls.append( (one, two) )


    not_pass = []
    for case in list(permutations(ls, 2)): #모두 비교해보면서
        print(case)
        
        # 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙
        # 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.
        if (case[0][0] < case[1][0]) and (case[0][1] < case[1][1]):
            if case[0] not in not_pass: #중복제거 위함
                not_pass.append(case[0]) 

    
    print(not_pass,'ㅎ') #얘네만큼은 절대 안뽑음

    print(len(ls) - len(not_pass))

    
