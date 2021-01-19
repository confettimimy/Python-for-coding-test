'''2016년 1월 1일은 금요일'''
def solution(a, b):
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    days = 0
    
    for i in range(1, a): # a월 이전까지의 날의 수 계산
        if i == 2:
            days += 29 # 윤년
        else: 
            if 1 <= i <= 7:
                if i % 2 != 0:
                    days += 31
                else:
                    days += 30
            elif 8 <= i <= 12:
                if i % 2 == 0:
                    days += 31
                else:
                    days += 30
                    
    days += b # 현재 a월에서의 날 수 계산
    days -= 1
    print(days)
    
    return week[days % 7] # 나머지
            
