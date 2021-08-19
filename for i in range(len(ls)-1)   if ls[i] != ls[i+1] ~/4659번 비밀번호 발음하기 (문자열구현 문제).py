

while True:
    s = input()
    if s=="end":
        break

    accept = True


    # [1]
    mo = False
    for c in s:
        if c in ('a', 'e', 'i', 'o', 'u'): #하나라도 모음이 있다면
            mo = True
            break
    if mo==True:
        pass
    else:
        accept = False
        

    # [2] 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    for i in range(len(s)-1-1):
        if s[i] in ('a', 'e', 'i', 'o', 'u'):
            #다음, 다다음것도 모음인지 검사하여본다.
            if s[i+1] in ('a', 'e', 'i', 'o', 'u') and s[i+2] in ('a', 'e', 'i', 'o', 'u'):
                #3개가 모음 연속인것.
                accept = False
                #print('2')

        if s[i] not in ('a', 'e', 'i', 'o', 'u'):
            #다음, 다다음것도 자음인지 검사하여본다.
            if s[i+1] not in ('a', 'e', 'i', 'o', 'u') and s[i+2] not in ('a', 'e', 'i', 'o', 'u'):
                #연속인것.
                accept = False
                #print('3')

                
    # [3]
    before = s[0] # e
    for i in range(1, len(s)): # eep
        if s[i]==before:
            if (before=='e' and s[i]=='e') or (before=='o' and s[i]=='o'):
                #print('4')
                pass
            else:
                accept = False
        before = s[i]


    if accept == True:
        print('<'+s+'>'+ ' is acceptable.')
    else:
        print('<'+s+'>'+ ' is not acceptable.')



'''다중반복문에서의 continue 사용에 버거움과 혼란을 느껴 accept=True/False 설정으로 바꾸었다..'''             
