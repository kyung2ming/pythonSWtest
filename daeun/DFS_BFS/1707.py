# https://www.acmicpc.net/problem/1707 이분 그래프
import sys
from collections import deque

T = int(input())
result = []


def bfs(v):
    queue = deque()
    queue.append(v)
    visit[v] = 1
    color[v] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visit[i] == 0:
                queue.append(i)
                color[i] = 3 - color[v]  # 색은 1 또는 2
                visit[i] = 1
            else:
                if color[v] == color[i]:
                    return False
    return True


while T > 0:
    T -= 1
    # 정점의 개수, 간선의 개수
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(V+1)]
    for i in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    visit = [0] * (V+1)
    color = [0] * (V+1)
    flag = True
    for j in range(1, V+1):
        if visit[j] == 0:
            if not bfs(j):
                flag = False
                break
    if flag:
        result.append("YES")
    else:
        result.append("NO")

for i in result:
    print(i)
