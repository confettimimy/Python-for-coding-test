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

# --------------------------
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
