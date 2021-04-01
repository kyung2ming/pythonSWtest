# https://www.acmicpc.net/problem/1260 DFS와 BFS
from collections import deque

# 정점개수, 간선개수, 시작정점번호
n, m, v = map(int, input().split())
graph = [[0]*(n+1) for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visit = [0] * (n+1)


def dfs(v):
    visit[v] = 1  # 방문처리
    print(v, end=' ')
    for i in range(1, n+1):
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = deque()
    queue.append(v)
    visit[v] = 0  # 초기화
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visit[i] == 1 and graph[v][i] == 1:
                queue.append(i)
                visit[i] = 0


dfs(v)
print()
bfs(v)
