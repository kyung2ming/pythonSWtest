import sys

sys.stdin = open('DYNAMIC/q4_input.txt')

if __name__ == "__main__":
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * n
    for i in range(n-1, -1, -1):

        if arr[i][0] + i <= n:

            dp[i] = max(dp[i+1], arr[i][1] + dp[i+arr[i][0]])

    print(dp)
