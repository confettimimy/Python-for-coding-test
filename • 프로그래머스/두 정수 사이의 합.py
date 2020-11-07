def solution(a, b):
    answer = 0
    
    if a == b:
        answer = a
    elif a > b:
        i = b
        while i <= a:
            answer += i
            i += 1
    elif a < b:    
        i = a
        while i <= b:
            answer += i
            i += 1
            
    return answer

# ------------------------------------------------
# by JAVA

class Solution {
  public long solution(int a, int b) {
      long answer = 0;
      long total = 0;
      if(a>b){
          int tmp = 0;
          tmp = a;
          a = b;
          b = tmp;
      }
      
      for(int start = a; start<=b; start++){
          total += start;
      }
      return total;
  }
}

# ------------------------------------------------
# Python re

def adder(a, b):
    
    if a > b: 
        a, b = b, a # C나 Java에서는 저장해둘 변수 tmp가 필요했지만 파이썬에서는 전혀 필요X

    return sum(range(a,b+1))

print( adder(3, 5))
