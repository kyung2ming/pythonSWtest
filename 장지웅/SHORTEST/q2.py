import sys
import heapq

sys.stdin = open("q2_input.txt")

n, e = map(int, input().split())

g = [[] for _ in range(n+1)]

for _ in range(1, e+1):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])


v1, v2 = map(int, input().split())


def dijkstra(start, end):
    distance = [sys.maxsize] * (n+1)
    q = []
    distance[start] = 0
    heapq.heappush(q, [0, start])

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in g[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

    return distance[end]


if dijkstra(1, n) == sys.maxsize:
    print(-1)

else:
    print(min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n),
              dijkstra(1, v2) + dijkstra(v1, v2) + dijkstra(v1, n)))

# 1번 정점에서 n번정점까지, 2개의 정점은 반드시 지남
