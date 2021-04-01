import sys
from queue import deque

sys.stdin = open("q2_input.txt")

n, m = map(int, input().split())

g = [[] for _ in range(n+1)]

visited = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


def DFS(v):
    if visited[v] == 1:
        return 0

    visited[v] = 1

    for vv in sorted(g[v]):
        DFS(vv)

    return 1


answer = 0
for i in range(1, n+1):
    answer += DFS(i)

print(answer)
