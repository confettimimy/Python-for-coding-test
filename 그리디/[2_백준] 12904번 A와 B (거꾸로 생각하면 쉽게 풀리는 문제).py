''' S를 T로 변경하고자 한다면 로직을 생각하기 어렵지만, T를 S로 변경하면 쉽게 풀리는 문제이다.
- S, T의 길이가 같을 때까지, 반복한다.
- T의 마지막 문자열이 A이면 pop한다.
- T의 마지막 문자열이 B이면 pop 후에, 문자열을 뒤집는다.'''

s = list(input())
t = list(input())


while True:
    if len(t) == len(s):
        break

    if t[-1] == 'A':
        t.pop()

    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    

if t == s:
    print(1)
else:
    print(0)
