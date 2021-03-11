import sys

sys.stdin = open('DYNAMIC/q1_input.txt')


if __name__ == "__main__":

    n = int(input())
    dp = [0] * (n + 1)

    dp[0] = 1

    for i in range(n):
        for j in range(i+1):
            dp[i+1] += dp[j] * dp[i-j]

    print(dp[n])
