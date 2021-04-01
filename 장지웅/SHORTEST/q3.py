import heapq
import sys

sys.stdin = open("q3_input.txt")

v, e = map(int, input().split())

k = int(input())

g = [[] for _ in range(v+1)]
distance = [sys.maxsize] * (v+1)

for i in range(e):
    a, b, c = map(int, input().split())
    g[a].append((b, c))


def dijkstra(start):

    q = []

    distance[start] = 0
    cost = 0
    heapq.heappush(q, [0, start])  # 코스트를 0으로 초기화 후 힙큐

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:  # visited 대용,
            continue

        for i in g[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

    return cost


dijkstra(k)
for i in distance[1:]:
    if i == sys.maxsize:
        print("INF")
    else:
        print(i)
