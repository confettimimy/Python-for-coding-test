from collections import Counter #시간 제한 1초이므로 해시 개념 사용하기
#dic = {} 

ls = []
cnt = 0
while True:
    cnt += 1
    tree = input()
    if tree=="": #입력이 없으면 종료 
        break
    
    ls.append(tree)
cnt-=1


counter = dict(Counter(ls))
print(counter)


#딕셔너리 자료형은 sort() attribute를 갖고있지 않으니까 리스트 자료형으로 바꾸기
arr = []
for sort in counter:
    arr.append( [sort, counter[sort]] )
print(arr)

# arr과 같이 리스트 자료형으로 바꿨으니 이제 sort()이용해서 사전순으로 정렬 가능
arr.sort()


# 각각의 종이 전체에서 차지하는 비율
for i in range(len(arr)):
    arr[i][1] = arr[i][1]*100/cnt # 갯수를 비율로 수정  #곱하기 나누기-> 괄호가 필요 없었음. 그렇게 하면 값이 아예 다르게 나옴.
    tmp_ls = str(arr[i][1]).split('.') #소수점 네번째자리까지만 표현하기 위해 문자열로 바꿔 접근. . . -> 반올림이라 문자열로 접근해서 버리면 안됨!
    tmp_ls2 = [ tmp_ls[0], tmp_ls[1][0:4] ]
    arr[i][1] = float(".".join(tmp_ls2))
print(arr)


# 이제 한줄씩 출력
for line in arr:
    print(line[0], line[1])
