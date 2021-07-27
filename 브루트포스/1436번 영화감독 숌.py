n = int(input()) # N은 10,000보다 작거나 같은 자연수

#1666 2666 3666...// 6660 6661 6662...6665 6666...6669 // 7666 8666 9666 10666

'''<다른 새로운 접근법> 노가다 하다가 (+예외도 일일이 처리해주고..) 값이 커질때의 경우를 생각못해 다른 접근법을 인터넷에서 찾아봤다.
666 부터 시작하여 1씩 증가시켜 해당 값이 666 을 포함하고 있다면 count값을 증가시킨다.
그리고 count 값이 N 이랑 같아질 경우 해당 num 이 N번째 숫자가 되는 것이다.

<문제풀이 후기>
num값을 1씩 계속 증가시켜 종말숫자임을 충족하면 그때 cnt를 올리는 방식으로 몇번째인 것을 세는 것이다.
숫자를 1씩 올려가며 찾는 전형적인 브루트포스 방식
'''

cnt = 0 # 몇 번째 - 종말숫자 충족할 때마다 +1된다. 즉, 
num = 665

while True:
    if cnt == n:
        print(num)
        break

    num+=1
    
    if '666' in str(num):
        cnt += 1
        #print(num,'충족될때') #확인용
        
        





''' <전에 했던 노가다(?)(일일이 예외처리해준 바보같은 방식>
num = '666'
cnt=1
k=1
while cnt<=10000:
    if cnt == n:
        print(num)
        break

    if num == '5666':
        num = '6660'
        #print(num,'상태체크 ')
        continue
    if num == '6669':
        num = '7666'
        #print(num,'상태체크 ')
        continue
    
        

    if len(num) == 3:
        num = ('1' + num)
    elif len(num) == 4:
        if num[1:4] == '666' and num != '6666':
            #print('1')
            tmp = num[0]
            tmp = str(int(num[0])+1) # '1'->'2'
            num = tmp + num[1:]          
        elif num[0:3] == '666' and int(num[-1]) < 9:
            print('2')
            num = '666' + str(k)
            k+=1

    #print(num,'상태체크 ')
    cnt+=1
'''

