# https://www.acmicpc.net/problem/13699 점화식
n = int(input())

# DP 테이블 초기화
d = [0] * 36

d[0] = 1
d[1] = 1
if n >= 2:
    for i in range(2, n+1):
        for j in range(i):
            d[i] += (d[j] * d[i-j-1])

print(d[n])
