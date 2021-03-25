r, c = map(int, input().split())


maps1 = [ list(input())  for _ in range(r)] # input() -> list( input() ) 문자열 요소는 변경이 안되니까 리스트 자료형으로 만들어버리기

maps2 = [input()  for _ in range(r)]



# 요소 변경해보기
maps1[0][0] = '@'
#maps2[1][0] = '^' # --> 아래 오류 메시지와 같이 문자열이라 문자열 요소 변경 불가능
'''[오류]   maps2[1][0] = '^'
TypeError: 'str' object does not support item assignment'''



print('maps1: ', maps1)
print('maps2: ', maps2)
'''
maps1:  [['@', '.', '.', '#', '.', '.'], ['.', '#', '#', 'v', '#', '.'], ['#', 'v', '.', '#', '.', '#'], ['#', '.', 'k', '#', '.', '#'], ['.', '#', '#', '#', '.', '#'], ['.', '.', '.', '#', '#', '#']]
maps2:  ['...#..', '.##v#.', '#v.#.#', '#.k#.#', '.###.#', '...###']

'''
