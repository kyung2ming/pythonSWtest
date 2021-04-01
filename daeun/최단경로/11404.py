# https://www.acmicpc.net/problem/11404 플로이드
import sys
INF = int(1e9)  # 무한으로 10억 설정

n = int(input())
m = int(input())

# 2차원 리스트 값을 모두 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("0", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
