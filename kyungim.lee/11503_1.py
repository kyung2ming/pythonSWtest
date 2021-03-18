# Baekjoon 가장 긴 증가하는 부분수열
# DP문제
from sys import stdin

# memo : Ai를 last value로 갖는 LIS
memo = [0 for _ in range(1111)]

if __name__ ==  '__main__':

    # 수열 A의 크기
    N = int(stdin.readline().strip())
    
    # 수열 A를 이루는 Ai
    A = [map(int, stdin.readline().strip().split(" ")) for _ in range(N)]

    memo[0]= 1
    for i in range(N):
        memo[i] = 1
        for j in range(i):
            if array[i] > array[j] and memo[j] + 1 > memo[i]:
                memo[i] = memo[j] +1
        if max < memo[i]:
            max = memo[i]

    print(max)