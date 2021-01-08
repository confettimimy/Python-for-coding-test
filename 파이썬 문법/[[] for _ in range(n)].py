# 첫 번째 예시
array = [[] for _ in range(10)]
array[0] = 0
print(array)
# 실행결과: [0, [], [], [], [], [], [], [], [], []]




# 두 번째 예시
array2 = [list(map(int, input().split(','))) for _ in range(5)]
'''1,1
   2,3
   3,4
   9,8
   5,2'''
for a in array2:
    print(a, end=' ')
# 실행결과: [1, 1] [2, 3] [3, 4] [9, 8] [5, 2] 




# 세 번째 예시
array3 = [input() for _ in range(5)]
'''백준
   온라인
   저지
   문제
   풀이'''
print(array3)
# 실행결과: ['백준', '온라인', '저지', '문제', '풀이']
    
