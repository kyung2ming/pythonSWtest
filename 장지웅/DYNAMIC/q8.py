import sys

sys.stdin = open('q8_input.txt')

n = int(input())

arr = list(list(map(int, input().split())) for _ in range(n))

dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    temp = arr[i][0] + i
    if temp <= n:
        dp[i] = max(arr[i][1] + dp[temp], dp[i+1])
    else:
        dp[i] = dp[i+1]
print(dp[0])
