import sys

sys.stdin = open('q6_input.txt')

n = int(input())

arr = [_ for _ in list(map(int, input().split()))]

dp = [0] * n

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
