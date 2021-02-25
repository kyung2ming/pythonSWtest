import sys
from collections import deque

sys.stdin = open("2178.txt", "rt")


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx <= n - 1):
                continue
            if not (0 <= ny <= m - 1):
                continue
            if g[nx][ny] == 0:
                continue

            if g[nx][ny] == 1:
                g[nx][ny] = g[x][y] + 1
                q.append((nx, ny))

    return g[n - 1][m - 1]


if __name__ == "__main__":
    n, m = map(int, input().split())
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    g = [0] * n
    for k in range(n):
        g[k] = list(map(int, input()))
    print(bfs(0, 0))
