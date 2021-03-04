import time
import sys
from collections import deque


start_time = time.time()
sys.stdin = open("DFSBFS/q5_input3.txt", "r")

# 코드


def bfs(x):
    queue = deque()
    queue.append(x)
    distance[x] = 0
    while queue:
        temp = queue.popleft()
        for _ in graph[temp]:
            if distance[_] == -1:
                distance[_] = distance[temp] + 1
                queue.append(_)


if __name__ == "__main__":

    n, m, k, x = map(int, input().split())

    distance = [-1] * (n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    bfs(x)

    answer = []

    for i in range(len(distance)):
        if distance[i] == k:
            answer.append(i)

    if not answer:
        print(-1)

    else:
        for _ in sorted(answer):
            print(_)


end_time = time.time()
# print(end_time-start_time)
