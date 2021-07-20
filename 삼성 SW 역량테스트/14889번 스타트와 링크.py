from itertools import combinations


n = int(input()) #짝수
S = []
for _ in range(n):
    S.append(list(map(int, input().split())))

start_score = 0 # 1 2
link_score = 0 # 3 4
arr = [i for i in range(1, n+1)]


possible = []
for case in list(combinations(arr, n//2)):
    start_team = list(case)
    link_team = []
    for a in arr:
        if a not in start_team:
            link_team.append(a)
    #start_team, link_team 팀 결성 -> 하나의 케이스
    #print(start_team, link_team) #[1, 2, 3] / [4, 5, 6]


    start_score = 0
    for two in combinations(start_team, 2):
        #print(two,'g')
        #two[0] two[1]  #(1, 2) / (2, 3) / (1, 3)
        start_score += S[two[0]-1][two[1]-1] + S[two[1]-1][two[0]-1] #s[1][2]
        
    link_score = 0
    for t in combinations(link_team, 2):
        #print(t,'dd')
        link_score += S[t[0]-1][t[1]-1] + S[t[1]-1][t[0]-1]
        
    #print(start_score, link_score)

    
    possible.append( abs(start_score-link_score) )


#print(possible)
print(min(possible))
