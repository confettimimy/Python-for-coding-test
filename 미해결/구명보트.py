#구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고
#무거운 사람들->너무 무거워서 혼자타거나 vs 가벼운사람과 합쳐 타거나
def solution(people, limit):
    people.sort(reverse=True) #[80 70 50 50]
    cnt = 0 #보트 개수
    copy = list(people)
    j= len(people)-1
    for i in range(len(people)):
        if sum(copy) <= limit:
            cnt +=1
            break
        if people[i]+people[j-i] <= limit and i<j:
            cnt +=1
            copy.remove(people[i])
            copy.remove(people[j-i])
        else: #무거운 사람 혼자타기
            cnt +=1
            copy.remove(people[i])
            j-=1
        #print(copy,cnt)
        
    return cnt
        
