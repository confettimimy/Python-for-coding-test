'''
파이썬에는 dir()이라는 내장 함수가 있다.
dir() 내장 함수는 어떤 객체를 인자로 넣어주면 해당 객체가 어떤 변수와 메소드(method)를 가지고 있는지 나열해준다.

예를들어 리스트라는 자료형이 어떤 메소드들을 가지고 있는지 기억이 안날때는 이 함수를 쓰면 좋다. 굳이 레퍼런스에서 복잡하게 안봐도!
'''



l = [1,2,3,4,5]


print( dir(l) )
#... 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print( dir(set(l)) )
#... 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
