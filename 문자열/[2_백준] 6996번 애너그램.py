t = int(input())

for _ in range(t):
    A, B = input().split()

    if len(A) != len(B):
        print(A, '&', B, "are NOT anagrams.")
        continue
    

    B_list = list(B)
    for a in A:
        if a in B_list:
            B_list.remove(a)

    if not B_list: # B가 비어있다면
        print(A, '&', B, "are anagrams.")
    else:
        print(A, '&', B, "are NOT anagrams.")
