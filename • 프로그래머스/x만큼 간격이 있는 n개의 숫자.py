def solution(x, n):
    ls = []
    tmp = x # x값 저장해놓기
    for _ in range(n):
        ls.append(x)
        x += tmp        
    return ls
