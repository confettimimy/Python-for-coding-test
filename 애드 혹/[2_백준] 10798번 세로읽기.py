matrix = []

for _ in range(5):
    matrix.append( list(input()) )
    # 줄마다 다른 길이의 문자열을 입력 받는다.


# 가장 긴 단어인 줄 max_line
max_line = max(list( len(matrix[k]) for k in range(5) ))
'''print(max_line)'''

# 맞춰주기. 레그드 배열이 아닌 정사각형 모양의 NXN 행렬 모양이 될 수 있도록 - 나중에 행 열 거꾸로 출력하기 편하게
for a in range(5):
    if len(matrix[a]) != max_line:
            matrix[a] += " "*(max_line-len(matrix[a]))

'''# ㄴ> 비어진 공간에 공백이 잘 넣어졌나 확인용
for i in range(5):
    for j in range(max_line):
        print(matrix[i][j], end='')
    print('')'''




# 세로로 출력
for j in range(max_line):
    for i in range(5):
        
        if matrix[i][j] == " ":
            continue
        
        print(matrix[i][j], end='')

