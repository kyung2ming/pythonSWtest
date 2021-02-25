import time
import sys
import path
import os
from collections import deque

# 코드

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs():
    count = [[0] * length for i in range(length)]
    queue.append([cur_x, cur_y])
    count[cur_x][cur_y] = 1

    while queue:
        x, y = queue.popleft()

        if x == mov_x and y == mov_y:
            print(count[mov_x][mov_y]-1)
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < length) and (0 <= ny < length) and (count[nx][ny] == 0):
                queue.append([nx, ny])
                count[nx][ny] = count[x][y] + 1


# input.txt 가공
start_time = time.time()
f = open(os.getcwd() + "/DFSBFS/q4_input.txt", "r")

data1 = f.readlines()

M = int(data1[0])
for i in range(M):
    data = data1[i*M+1:i*M+4]

    length = int(data[0])
    cur_x = int(data[1].split()[0])
    cur_y = int(data[1].split()[1])
    mov_x = int(data[2].split()[0])
    mov_y = int(data[2].split()[1])

    queue = deque()
    bfs()


f.close()
end_time = time.time()
# print(end_time-start_time)
