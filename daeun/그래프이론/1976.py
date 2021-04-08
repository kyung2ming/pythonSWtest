# https://www.acmicpc.net/problem/1976 여행 가자
import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
M = int(input())
parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

cycle = True

for i in range(N):
    graph = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if graph[j] == 1:
            union_parent(parent, i+1, j+1)
plan = list(map(int, sys.stdin.readline().split()))
for i in range(len(plan)-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        print('NO')
        cycle = False
        break
if cycle:
    print('YES')


