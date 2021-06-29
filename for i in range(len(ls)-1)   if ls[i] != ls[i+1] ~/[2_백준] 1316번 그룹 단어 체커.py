n= int(input())
words=[]
for _ in range(n):
    words.append( input() )


count = 0 # 그룹단어의 개수
for word in words:
    
    chk = True
    #word = aabbbccb / aba
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:] : ####(이 부분을 인터넷 참조 해서 해결) 'a'가 뒤에 또나타나면 안되므로 
                #해당 word는 그룹단어가 아님.
                chk = False
                break


    if chk == True: #여전히 True라면 = 위 조건에 한번이라도 들지 않았다면
        count += 1
    


print(count)

'''플러스로,
for문의 현재 i 참조 실행중
i+1 이렇게 다음이나 이전 것을 참조하고 비교하는 것도 가능하지만
위 #### 부분과 같이 word[i+1 : ] 이런식으로 아예 여러 이후값 자체도 참조 가능.
즉 현재 단어구 안의 문자 하나에 아무거나에 자유자재로 접근할 수 있다는 뜻임.'''
