# https://www.acmicpc.net/problem/11053 가장 긴 증가하는 부분 수열
import sys

n = int(input())
array = list(map(int, sys.stdin.readline().split()))

# DP 테이블 초기화
d = [0] * n

for i in range(n):
    for j in range(i):
        if array[j] < array[i] and d[j] > d[i]:
            d[i] = d[j]
    d[i] += 1

print(max(d))
