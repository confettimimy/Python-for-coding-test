def solution(arr):
    answer = []

    for i in range(len(arr)):
        if i==0: #배열의 첫번째 원소는 이전 원소가 없으니 비교할 수 없다
            answer.append(arr[i])
            continue
        elif arr[i] == arr[i-1]:#이전 원소와 같으면
            continue #아래 실행하지 말기 -> answer배열에 추가시키지 말기
        answer.append(arr[i])

    return answer

# 중복제거이기 때문에 집합 자료형을 이용해 중복을 제거하려 했지만 문제 조건의 배열 원소들의 순서를 유지해야 한다는 조건 때문에 집합 자료형을 이용하지 못했다. 집합 자료형은 순서X이기 때문.