
while True:
    s = input()
    if s == "0":
        break

    if list(s) == list(reversed(s)):
        print("yes")
    else:
        print("no")
    
