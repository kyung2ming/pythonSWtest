import sys
import heapq

sys.stdin = open("1504.txt", "rt")

n, e = map(int, input().split())
INF = int(1e9)
g = [[] for i in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (n + 1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in g[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


# 1 -> v1 -> v2 -> n
# 1 -> v2 -> v1 -> n

compare1 = dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[n]
compare2 = dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[n]


result = min(compare1, compare2)
if result >= INF:
    print(-1)
else:
    print(result)
