# Baekjoon 가장 긴 증가하는 부분수열
# DP문제
from sys import stdin

# memo[0][0 - 1111] : Ai를 last value로 갖는 LIS
# memo[1][0 - 1111] : LIS의 last value 중 minimum
memo = [[0]*1111 for _ in range(1111)]

if __name__ ==  '__main__':

    # 수열 A의 크기
    N = int(stdin.readline().strip())

    # 수열 A를 이루는 Ai
    A = list(map(int, stdin.readline().strip().split(" ")))
    A.insert(0, 0)

    memo[0][1] = 1
    memo[1][1] = A[1]
    for i in range(1, N):
        curI = A[i]

        for j in range(0, i):
            if memo[1][j] < curI:
                memo[0][i] = memo[1][j] + 1
                memo[1][j+1] = curI

    print(memo[1])