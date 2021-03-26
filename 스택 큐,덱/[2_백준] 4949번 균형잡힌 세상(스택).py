while True:
    s = input()

    if s == ".":
        break

    answer = "yes"
    stack = [] 



    for c in s:
        if c == '(' or c == '[':
            stack.append(c)


        if c == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                answer = "no"
                break
        elif c == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                answer = "no"
                break


        
    if stack:
        answer = "no" ###


    print(answer)


