import time
import sys
import path
import os
from collections import deque

# input.txt 가공
start_time = time.time()
f = open(os.getcwd() + "/DFSBFS/q1_input2.txt", "r")

data = f.readlines()

M, N = map(int, data[0].split())
data = data[1:]
box, queue = [], deque()
for i in range(len(data)):
    row = data[i].split()

    box.append(list(map(int, row)))
    for j in range(len(row)):
        if row[j] == "1":
            queue.append([i, j])


# print(box)
# print(M)
# print(N)
# print(queue)
# 코드
'''
    m = 가로, n = 세로
    graph = 2차원 배열
'''


def bfs(M, N, box):
    # 좌우상하
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    days = -1

    # 모든 스택을 다 빼줌
    while ripe:
        print(ripe)
        days += 1
        for _ in range(len(ripe)):
            x, y = ripe.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx < N) and (0 <= ny < M) and (box[nx][ny] == 0):
                    box[nx][ny] = box[x][y] + 1
                    ripe.append([nx, ny])

    for b in box:
        if 0 in b:
            return -1
    return days
# def bfs():
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]

#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             print(ny)


print(bfs())
