t = int(input())

for _ in range(t):
    s = input()

    stack = []

    for c in s:
        if c == ')':
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            elif len(stack)==0:
                stack.append(c)
            continue # if c == ')':문에 걸리면
        
        stack.append(c)
        
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")

    
