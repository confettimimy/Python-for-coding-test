s = input()

new_s = ''
for c in s:
    if c == ' ':
        new_s += ' '
        continue
    if c.isdigit():
        new_s += c
        continue
    
    nb = ord(c)+13
    if 65<=ord(c)<=90 and ord(c)+13 >90: #대문자 
        nb = 65 + (13 - (90-ord(c))) -1
    elif 97<=ord(c)<=122 and ord(c)+13 >122: #소문자
        nb = 97 + (13 - (122-ord(c))) -1
    new_s += chr(nb)

print(new_s)
