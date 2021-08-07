pan = []
for _ in range(5):
    pan.append( list(map(int, input().split())) )
call = []
for _ in range(5):
    call.append( list(map(int, input().split())) )


count = 0
i=0
j=0
bump = 0 #한줄 빙고
history1 = []
history2 = []
o=False
t=False
while count<=25:
    #print(i,j,'i,j') #아래 i,j 카운팅 부분 들여쓰기 질못해서 index out 오류난거였음

    count += 1

    for a in range(5):
        if call[i][j] in pan[a]: # pan 한줄마다
            pan[a][ pan[a].index(call[i][j]) ] = 0

            #아래는 조건탐색

            #행 한줄 확인
            for l in range(5):
                if pan[l] == [0,0,0,0,0]:
                    if l not in history1:
                        bump +=1
                        history1.append(l)
                        if bump == 3:
                            print(count)
                            exit()

            #열 한줄 확인
            for yul in range(5):
                
                tmp = []
                for m in range(5):
                    tmp.append(pan[m][yul])
                if tmp == [0,0,0,0,0]:
                    if yul not in history2:
                        bump += 1
                        history2.append(yul)
                        if bump == 3:
                            print(count)
                            exit()

            #대각선 한줄
            one = [pan[c][c] for c in range(0, 5)]
            two = [pan[d][4-d] for d in range(0, 5)]
            if one == [0,0,0,0,0]:
                if o ==False:
                    bump += 1
                    o=True
                    if bump == 3:
                        print(count)
                        exit()
                    
            if two == [0,0,0,0,0]:
                if t ==False:
                    bump += 1
                    t=True
                    if bump == 3:
                        print(count)
                        exit()

    if j == 4:
        i+= 1
        j=0
        continue
    j+=1
                    

#end
'''
- 구현 그 자체였던 문제였다.
- break는 한 루프만 빠져나가는것이기 때문에 위와 같이 if bump==3: 최종조건 만족후 출력만 하면 되는 상황일때 그냥 exit() 써버려도 된다. 그렇게 써도 맞습니다 라고 채점결과 나옴!
exit()
- 중간중간 자잘한 오류를 해결해나가며 구현을 완료하였다.
'''
        
        
