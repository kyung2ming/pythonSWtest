
from sys import stdin

dp = [[0]*4444 for _ in range(4444)]

if __name__ == '__main__':

    A = '0' + stdin.readline().strip()
    B = '1' + stdin.readline().strip()

    _max = 0
    for i in range(1, len(A)):
        for j in range(1, len(B)):
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1] + 1
                _max = max(dp[i][j], _max)

    print(_max)
