def solution(n, words):
    stack = [] # 끝말잇기 게임 성공한 단어들
    
    before = ""
    who = 0
    fail = True
    for word in words:
        if not stack: # 스택이 비어있다면 = 첫번째일 경우
            stack.append(word)
            
        if stack:
            if stack[-1][-1] == word[0] and word not in stack:
                stack.append(word)
            else:
                fail = False
                print(stack)
                
    if (len(stack)+1) % n == 0:
        who = n
    else:
        who = (len(stack)+1) % n
    print(who)
    
    return [who, (len(stack)+1)//n]
        

print( solution(3, [["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]]) )

