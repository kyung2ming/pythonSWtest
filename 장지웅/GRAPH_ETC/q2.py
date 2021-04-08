import sys
import heapq

sys.stdin = open("q2_input1.txt")


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_find(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())  # v < 10,000, e < 100,000

parent = [i for i in range(v+1)]
q = []

for _ in range(e):
    a, b, c = map(int, input().split())
    if a > b:  # 무향그래프
        a, b = b, a
    heapq.heappush(q, (c, [a, b]))  # 가중치로 오름차순 정렬

answer = 0
while q:
    cost, edge = heapq.heappop(q)

    if find_parent(edge[0]) != find_parent(edge[1]):
        union_find(edge[0], edge[1])
        answer += cost

print(answer)
