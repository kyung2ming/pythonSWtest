import sys
from collections import deque

sys.stdin = open("18352.txt", "rt")


def bfs(start, dest):
    q = deque()
    q.append((start, 0))
    visited[start] = 1

    while q:
        tmp, count = q.popleft()
        if count == dest:
            res.append(tmp)
        elif count < dest:
            for next_node in g[tmp]:
                if visited[next_node] == 0:
                    visited[next_node] = 1
                    q.append((next_node, count + 1))

            # for i in range(1, n + 1):
            #     if g[tmp][i] == 1 and visited[i] == 0:
            #         visited[i] = 1
            #         q.append((i, count+1))


if __name__ == "__main__":
    #
    # input = sys.stdin.readline
    n, m, k, x = map(int, input().split())
    # g = [[0] * (n + 1) for _ in range(n + 1)]
    g = [[] for _ in range(n+1)]
    visited = [0] * (n + 1)
    res = []
    for _ in range(m):
        a, b = map(int, input().split())
        # g[a][b] = 1
        g[a].append(b)

    bfs(x, k)
    res.sort()
    if not res:
        print(-1)
    else:
        for x in res:
            print(x)
