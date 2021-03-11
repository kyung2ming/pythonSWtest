# https://www.acmicpc.net/problem/1463 1로 만들기
n = int(input())

# DP 테이블 초기화
d = [0] * (n+1)

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)

print(d[n])
