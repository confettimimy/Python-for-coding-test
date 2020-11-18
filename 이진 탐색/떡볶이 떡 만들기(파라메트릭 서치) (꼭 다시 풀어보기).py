# 절단기의 높이(탐색 범위)는 1부터 10억까지의 정수 중 하나인데, 이처럼 큰 수를 보면 당연하다는 듯이 가장 먼저 이진탐색을 떠올려야 한다.
# 이 문제에서 절단기의 높이 범위가 한정적이었다면 순차탐색으로도 해결할 수 있지만, 현재 문제에서 절단기의 높이는 최대 10억까지의 정수이므로 순차탐색 방식은 분명 시간초과를 받을 것이다.

n, m = map(int, input().split()) # m은 요청한 떡의 길이
array = list(map(int, input().split()))

# 이진탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진탐색 수행(반복적으로 구현이 더 간결)
result = 0
while(start <= end):
    total = 0 # 잘린 떡의 길이들을 모두 더해 저장해놓는 변수

    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += (x-mid)

    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1


# 정답 출력
print(result)
    
