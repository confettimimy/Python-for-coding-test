s = input()


for i in range(26): # 소문자 알파벳은 총 26개
    #print(chr(i+97),'확인용')
    
    if chr(i+97) in s: # chr(i+97), 즉 a부터 하나씩 순차적으로 확인
        print(s.index(chr(i+97)), end=' ')
    else:
        print(-1, end=' ')

