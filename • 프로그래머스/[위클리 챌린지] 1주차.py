def solution(price, money, count):
    cost = 0
    for i in range(1, count+1): # 3 6 9 12
        tmp_price = price # 원래 이용료의
        tmp_price *= i # n배
        cost += tmp_price
    
    if cost >= money:
        return (cost - money)
    else:
        return 0
