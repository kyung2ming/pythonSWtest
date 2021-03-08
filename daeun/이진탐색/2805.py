# https://www.acmicpc.net/problem/2805 나무 자르기
# Python 3로 제출하면 시간초과, PyPy3로 제출함
import sys
n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(array)
result = 0

# 이진 탐색
while start <= end:
    total = 0  # 잘린 나무 총 합
    mid = (start + end) // 2
    for tree in array:
        if tree > mid:
            total += (tree - mid)
    if total < m:
        end = mid - 1  # 더 많이 자름
    else:
        result = mid
        start = mid + 1  # 더 조금 자름

print(result)
