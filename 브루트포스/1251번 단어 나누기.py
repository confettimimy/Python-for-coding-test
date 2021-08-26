from itertools import product #중복순열

word = input()



cnt = len(word)
nums = [i for i in range(1, cnt-1)]

possible = []
for case in list(set(product(nums, repeat=3))):
    if sum(case) == cnt:
        #print(case) #단어 쪼개기

        tmp = [[], [], []]
        i = 0 # word = mobitel
        for _ in range(case[0]):
            tmp[0].append(word[i])
            i+=1
        for _ in range(case[1]):
            tmp[1].append(word[i])
            i+=1
        for _ in range(case[2]):
            tmp[2].append(word[i])
            i+=1
        #print(tmp)


        answer = ''
        # 각각 뒤집고 합치기
        for p in range(len(tmp)):
            tmp[p] = list(reversed(tmp[p]))
            answer += "".join(tmp[p])
        possible.append(answer)


possible.sort()
#print(possible)
print(possible[0])
