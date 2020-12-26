k = int(input())

stack = []

for _ in range(k):
    n = int(input())
    if n == 0 and len(stack) > 0:
        stack.pop() # 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고
    else: # 아닐 경우 해당 수를 쓴다.
        stack.append(n)

print(sum(stack))
        
