# 입출력 예시를 통해 리스트A의 가장 작은 원소와 리스트B의 가장 큰 원소(혹은 그 반대)를 곱하면 된다고 판단 -> 정렬을 이용
def solution(A,B):
    
    A.sort()
    B.sort(reverse = True)
    
    answer = 0
    for i in range(len(A)):
        answer += (A[i] * B[i])

    return answer

