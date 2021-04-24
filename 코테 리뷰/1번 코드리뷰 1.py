# 접속 날짜
access_dates = ["05/30", "05/31", "06/01", "06/02",   "06/05", "06/06", "06/07", "06/08", "06/09"]

start_date = "05/01 MON"
end_date = "05/30 MON"


def solution(start_date, end_date, access_dates ):
    # /를 기준으로 split
    ls = [] # access_dates 요소들을 정제해 넣어두는 리스트
    for date in access_dates:
        ls.append( int("".join(date.split("/"))) )
    print(ls)

    
    save = [] 
    # 연속이 끊기는 지점을 찾아 표시해두기
    for i in ls:
        
    


solution(start_date, end_date, access_dates)





'''
연속접속 날짜 중 가장 긴 최대일수를 구하여라.
단, 연속된 날짜 중 토요일, 일요일 주말은 제외한 만큼의 수를 상으로 줘라.



문자열 문제 / 구현을 계속 진행하다가 시간이 없어서 끊긴 문제.



"/", " "을 기준으로 split해서 숫자로 합침!
숫자로 바꿔서 연속되는 기간들 뺄려고...


주말은 연속일수에서 빼려면
해당 일이 몇요일인지 파악해야함!!!



연속이 끊기는 부분을 찾으려다가 이 부분에서 계속 오류나고 끝남!
연속이 끊기는 부분 따로 구현하며 공부해보

'''
    
