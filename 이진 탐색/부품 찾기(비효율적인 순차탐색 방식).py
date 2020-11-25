''' 본인은 순차탐색을 이용해 해당 문제를 해결하였다.
    SK코딩테스트에서는 참조가 불가능하여 이진탐색 알고리즘을
    잘 외우지 못했을 경우를 대비해 내 스스로 현장에서 구현할 수 있는
    순차탐색을 택해 문제를 해결했다.
    하지만 이진탐색 알고리즘을 현장에서 정확하게 구현할 수 있거나,
    현장에서 참조가 가능하다면 이진탐색을 이용해 푸는 것이 시간복잡도면에서는 당연 효율적일 것이다.
'''

def data_search(arr, target, num):

  t = False
  for i in range(num): #데이터 탐색을 위해 순차탐색 이용
    if arr[i] == target:
      t =True
  
  if t == True:
    return "yes"
  elif t == False:
    return "no"
    


n = int(input()) #가게의 부품 총 개수
all_list = list( map(int, input().split()) )

m = int(input()) #찾고자 하는 부품 번호들 나열
target_list = list( map(int, input().split()) )



for i in range(m):
  print(data_search(all_list, target_list[i], len(all_list)), end=" ")

