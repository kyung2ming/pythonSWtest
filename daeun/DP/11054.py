# https://www.acmicpc.net/problem/11054 가장 긴 바이토닉 부분 수열
import sys

n = int(input())
array = list(map(int, sys.stdin.readline().split()))

# DP 테이블 초기화
inc = [1] * n
dec = [1] * n

result = [0] * n

# 최대 증가 부분수열 길이
for i in range(n):
    for j in range(i):
        if array[j] < array[i] and inc[i] < (inc[j] + 1):
            inc[i] = inc[j] + 1

# 최대 감소 부분수열 길이
for i in reversed(range(n)):
    for j in range(i+1, n):
        if array[j] < array[i] and dec[i] < (dec[j] + 1):
            dec[i] = dec[j] + 1

# 최대 증가 부분수열 길이 + 최대 감소 부분수열 길이 - 1
for i in range(n):
    result[i] = dec[i] + inc[i] - 1

print(max(result))


