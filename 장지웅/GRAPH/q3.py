import sys
from queue import deque

sys.stdin = open("q3_input.txt")

K = int(input())


def bfs(n, color):

    q.append(n)

    while q:
        v = q.popleft()

        v_color[n] = color

        color *= -1

        for vv in g[v]:
            if v_color[vv] == color:  # 인접한 정점이 색이 같을 때
                return True
            elif v_color[vv] == 0:
                q.append(vv)

        print(v)
    return False


for _ in range(K):

    v, e = map(int, input().split())

    g = [[] for __ in range(v+1)]
    parent_list = [__ for __ in range(v+1)]

    for __ in range(e):
        a, b = map(int, input().split())

        g[a].append(b)
        g[b].append(a)

    q = deque()
    for i in range(1, (v+1)):
        v_color = [0] * (v+1)  # 0 미방문 1, -1 색

    if bfs(i, 1):
        print("NO")
    else:
        print("YES")
