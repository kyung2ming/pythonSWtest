# https://www.acmicpc.net/problem/11724 연결 요소의 개수
import sys
sys.setrecursionlimit(10000)  # 런타임 에러 방지
# 정점개수, 간선개수
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visit = [0] * (n+1)


def dfs(v):
    visit[v] = 1  # 방문처리
    for i in graph[v]:
        if visit[i] == 0:
            dfs(i)


count = 0
for i in range(1, n+1):
    if visit[i] == 0:
        dfs(i)
        count += 1

print(count)
