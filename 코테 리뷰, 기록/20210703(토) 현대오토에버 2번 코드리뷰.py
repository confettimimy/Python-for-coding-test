# 현대오토에버 2번 최종답안 - 테케 다 맞춤
def solution(ip_addrs, langs, scores):
    same = ['C','C++','C#']

    ip = list(set(ip_addrs))
    dic = {}
    for k in ip:
        dic[k] = 0 #딕셔너리 초기화

    for i in range(len(ip_addrs)):
        if ip_addrs[i] in ip:
            dic[ip_addrs[i]] += 1
    #print(dic) #확인용
    error = [] #지울애들. remove해버리먄 인덱스가 중간에 바뀜
    for one in dic.keys():

        if dic[one] >= 4: # [조건1]
            for ip in ip_addrs: #모두지우기
                if ip == one:
                    error.append(ip)

        elif dic[one] == 3: #[조건2]
            lang_check = []#같은언어 사용 확인
            for p in range(0, len(ip_addrs)): #3명으로만 추려야함
                if ip_addrs[p] == one:
                    lang_check.append( langs[p] )
            lang_distinct =[]
            for l in lang_check:
                if l not in lang_check and l in ['Java', 'JavaScript', 'Python3']:
                    lang_distinct.append(l)
                elif l in same:
                    lang_distinct.append('C')
            lang_distinct = list(set(lang_distinct))
            if len(lang_distinct) == 1: #모두 같은 언어를 사용했을 경우
                #3명 모두 부정참가자
                for ip in ip_addrs:
                    if ip == one:
                        error.append(ip)

        elif dic[one] == 2: #[조건3]  '5.5.5.5'
            lang_check2 = []
            for p in range(0, len(ip_addrs)):
                if ip_addrs[p] == one:
                    lang_check2.append( langs[p] )
            lang_distinct2 = []
            for l in lang_check2:
                if l in same:
                    lang_distinct2.append('C')
                elif l in ['Java', 'JavaScript', 'Python3']:
                    lang_distinct2.append(l)

            if len(list(set(lang_distinct2))) == 1: # (1)두명이 같은 언어군을 사용했고,
                # (2)성적도 동일할때의 처리
                score_distinct = []
                for q in range(len(ip_addrs)):
                    if ip_addrs[q] == one:
                        score_distinct.append( scores[q] )
                if score_distinct[0]==score_distinct[1]:#어차피두개니까
                    for x in range(len(scores)):
                        if scores[x] == score_distinct[0]:
                            error.append(ip_addrs[x])



    #print(error, '버릴애들')          
    return (len(ip_addrs)-len(error))

