
i=1
while True:
    s = list(input()) # }}{{
    if '-' in s:
        break

    oper_num = 0 #필요한 연산 수

    stack = []
    close = []
    for c in s:
        if c=='{':
            stack.append('{')
        elif len(stack) != 0:
            stack.pop()
            close.append('}')
    #print(stack)
    
    if len(stack)!=0: # {{
        if len(close) == len(stack) and len(close)!=1 and len(stack)!=1:
            oper_num += len(close)
        elif len(close) == len(stack) and len(close)==1 and len(stack)==1:
            oper_num += 2
            continue
        
        if len(stack)%2==0:
            if stack.count('{') == len(stack): # 남은 요소가 모두 { 라면
                oper_num += (stack.count('{')//2)






    print(str(i)+'. '+ str(oper_num))
    i+=1
