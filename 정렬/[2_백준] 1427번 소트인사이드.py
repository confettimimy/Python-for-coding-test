s = input()

ls = []
for i in s:
    ls.append(int(i))

ls.sort(reverse = True)

ls = map(str, ls)
'''<오류>  print("".join(ls))
TypeError: sequence item 0: expected str instance, int found'''

print("".join(ls))
