import sys
from queue import deque

sys.stdin = open("q1_input.txt")

n, m, v = map(int, input().split())

g = [[] for _ in range(n+1)]


def DFS(v):
    if visited[v] == 1:
        return

    visited[v] = 1

    dfs_print.append(v)

    for vv in sorted(g[v]):
        DFS(vv)


def BFS(v):
    q.append(v)

    while q:

        vv = q.popleft()
        bfs_print.append(vv)
        visited[vv] = 1

        for vvv in sorted(g[vv]):
            if visited[vvv] != 1:
                visited[vvv] = 1
                q.append(vvv)


for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [0 for _ in range(n+1)]

dfs_print = []
bfs_print = []

DFS(v)

visited = [0 for _ in range(n+1)]

q = deque()

BFS(v)

print(' '.join(map(str, dfs_print)))
print(' '.join(map(str, bfs_print)))
