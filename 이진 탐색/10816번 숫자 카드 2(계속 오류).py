'''처음엔 이진탐색을 이용하여 문제를 해결하려고 했다. 최대한 고민하며 효율적으로 이진탐색을 구현해 봐도 게속 시간초과가 발생했고, 이유는 단일 target을 탐색할때는 당연히 이분탐색이 빠르지만, 이 문제에서는 target이 여러개 이고, 중복도 존재한다. 따라서 최초에 counting을 1번 해놓고, 탐색이 아닌 그냥 key값으로 value를 뽑아오는게 더 효율적이었다.'''

def binary_search(array, target, start, end):
    
    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1

    return None



n = int(input())
ls = list(map(int, input().split())) # 숫자 카드에 적혀있는 정수

m = int(input())
target = list(map(int, input().split())) # 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수
print(target)
count = 0


for k in target:
    count = 0

    target_index = binary_search(ls, k, 0, n-1)
    print('target', k)
    while target_index != None: # 타깃값이 ls안에 있다면
        count +=1
        print(target_index)
        ls.remove( ls[target_index] )
        n -= 1 # ls안의 요소값 개수가 제거함으로써 계속 바뀌기 때문에 이 처리를 해주어야함
        # while문 한 번 나오면 끝인가..ㅋㅋ 위에 while문 제목이 실행이 안되는거같은데
        print(ls, 'n=', n)
        print('while문 실행 ㅋ')

    print(count, end=' ')


    
