# 단, 주어진 number의 기존 순서대로 출력시켜야 한다. (입출력 예를 보고 다시 앎)
def solution(number, k):
    
    for _ in range(k): # k번 반복
        
        
        ls = list(map(int, number))
        small = min(ls) # 가장 작은값 넣어두기
        
        for i in number:
            if i == str(small):
                idx = number.index(i) ### 은근 많이 쓰이는 index()
                number = number[0:idx] + number[idx+1:len(number)]
                break # 하나 지우면 바로 나가기 (해당 그 수를 다 지워버리면 'k개수 제거'라는 문제조건에 부합하지 않게 될 수도 있음)
    
    
    return number
    
