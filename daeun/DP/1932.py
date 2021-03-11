# https://www.acmicpc.net/problem/1932 정수 삼각형
import sys

n = int(input())
d = []
for i in range(n):
    d.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(len(d[i])):
        if j == 0:
            d[i][j] += d[i-1][j]
        elif j == i:
            d[i][j] += d[i-1][j-1]
        else:
            d[i][j] += max(d[i-1][j-1], d[i-1][j])

print(max(d[n-1]))
