# Baekjoon 가장 긴 증가하는 부분수열
# DP문제
from sys import stdin

# memo : Ai를 last value로 갖는 LIS
memo = [0 for _ in range(1111)]

if __name__ == '__main__':

    # 수열 A의 크기
    N = int(stdin.readline().strip())

    # 수열 A를 이루는 Ai
    A = list(map(int, stdin.readline().strip().split(" ")))

    memo[0] = 1
    _max = 0

    for i in range(N):
        memo[i] = 1
        for j in range(i):
            if A[i] > A[j] and memo[j] + 1 > memo[i]:
                memo[i] = memo[j] + 1
        if _max < memo[i]:
            _max = memo[i]

    print(_max)