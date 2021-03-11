import sys

sys.stdin = open('DYNAMIC/q2_input.txt')

if __name__ == "__main__":
    n = int(input())
    dp = [0] * (n + 1)

    for i in range(2, n+1):
        dp[i] = min(dp[i-1], dp[i//2] if i % 2 == 0 else sys.maxsize,
                    dp[i//3] if i % 3 == 0 else sys.maxsize) + 1
    print(dp[n])
