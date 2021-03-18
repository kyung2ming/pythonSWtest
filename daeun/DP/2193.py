# https://www.acmicpc.net/problem/2193 이친수
n = int(input())

# DP 테이블 초기화
d = [0] * (n+1)

d[1] = 1
for i in range(2, n+1):
    d[i] = d[i-2] * 2 + (d[i-1] - d[i-2])

print(d[n])
