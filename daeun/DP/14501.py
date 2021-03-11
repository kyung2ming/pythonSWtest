# https://www.acmicpc.net/problem/14501 퇴사
import sys

n = int(input())
t_list = []
p_list = []

for i in range(n):
    t, p = map(int, sys.stdin.readline().split())
    t_list.append(t)
    p_list.append(p)

# DP 테이블 초기화
d = [0] * n

for i in range(n):
    if i + t_list[i] <= n:  # 상담이 끝나는 날짜 <= 최대 날짜(n)
        d[i] = p_list[i]
        for j in range(i):
            if j + t_list[j] <= i:
                d[i] = max(d[i], d[j] + p_list[i])

print(max(d))
