import sys
import heapq

sys.stdin = open("q4_input.txt")

n = int(input())  # 정점
m = int(input())  # 간선

g = [[] for _ in range(n+1)]
distance = [sys.maxsize] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append([b, c])


def dijkstra(start, end):
    distance[start] = 0  # 시작점 초기화

    q = []

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


s, e = map(int, input().split())
print(dijkstra(s, e))
