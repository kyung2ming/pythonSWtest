import sys

sys.stdin = open("11404.txt", "rt")
# input = sys.stdin.readline()

INF = int(1e9)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

g = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            g[a][b] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if g[a][b] > c:
        g[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            g[a][b] = min(g[a][b], g[a][k] + g[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if g[a][b] == INF:
            print(0, end=' ')
        else:
            print(g[a][b], end=' ')
    print()
