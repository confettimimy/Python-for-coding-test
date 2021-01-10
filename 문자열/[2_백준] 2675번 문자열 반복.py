t = int(input())
      
for _ in range(t):
      r, s = input().split()
      r = int(r)

      # 출력
      for c in s:
          print(c * r, end='')
      print('')
