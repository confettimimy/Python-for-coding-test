s = input()


alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']


for t in alpha:
    s = s.replace(t, '*') # s= 이 부분을 반드시 넣어줘야함 

#print(s)

print(len(s))
