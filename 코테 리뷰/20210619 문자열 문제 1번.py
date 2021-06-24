def solution(S, C):
    answer = ""
    email_ls = []
    

    S = S.split(', ')
    #print(S)
    number = 1

    for i in range(len(S)):
        S[i] += ' '

        email = "<"
        tmp_ls = S[i].split(' ')
        tmp_ls.pop()
        # 중간에 있는 -를 빼야함
        #print(tmp_ls,'1')
        for k in range(len(tmp_ls)):
            if "-" in tmp_ls[k]:
                tmp_ls[k] = tmp_ls[k].split('-')
                for j in range(len(tmp_ls[k])):
                    tmp_ls[k][j] = tmp_ls[k][j].lower()
                tmp_ls[k] = "".join(tmp_ls[k]) # 원본을 바꾸는 방식
        #print(tmp_ls,"2")
                
        email += tmp_ls[0].lower() + '.' + tmp_ls[-1].lower()
        email += "@" + C[0].lower() + C[1:] + ".com>"




        # 이제 같은 이메일을 갖고있는 것들을 2, 3과 같은 숫자를 붙여줌으로써 식별해야함! 여기서 계속 걸렸음
        tmp2 = []
        
        if email in email_ls: # ex: <john.doe@example.com> -> <john.doe2@example.com>
            tmp2 = email.split("@")

            duplication_estimation = dict() #두 개 이상인 중복메일 넣어둘 곳
            
            # '<john.doe @ example.com>'
            if tmp2[0][-1].isdigit() == True: #숫자가 있고 =이 경우 세번째 등장부터만 가능
                if int(tmp2[0][-1]) >= 2: #중복됐다면 / 2이면 현재가 3번째 등장이란 뜻 !
                    duplication_estimation[email] += 1
                    
            elif tmp2[0][-1].isalpha() == True and email not in duplication_estimation.keys(): #'<john.doe@example.com>' 이와 같이 숫자가 없는 경우
                duplication_estimation[email] = 1
                print(duplication_estimation,'~') #출력시켜보니까 다 여기에 들어가넹..
                
            elif tmp2[0][-1].isalpha() == True and email in duplication_estimation.keys(): # 두번째 등장의 경우는 여기에 정리
                duplication_estimation[email] = 2


            print(duplication_estimation,'><')
            tmp2[0] = tmp2[0] + str(duplication_estimation[email]) + "@"
            email = "".join(tmp2)

        email_ls.append(email)

    

        # 최종통과되면 최종 답 문자열에 이어붙이기
        S[i] += email_ls[i]

    print(email_ls)### 확인용


    
    #print(S) #S는 현재 문자열 요소로 구성된 리스트
    answer = ", ".join(S)
    
    return answer
    


    


print(  solution('John Doe, Peter Benjamin Parker, Mary Jane Watson-Parker, John Elvis Doe, John Evan Doe, Jane Doe, Peter Brian Parker', 'Example')  )
