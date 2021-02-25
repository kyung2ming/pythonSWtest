import time
import sys
import path
import os
from collections import deque

# input.txt 가공
start_time = time.time()
f = open(os.getcwd() + "/DFSBFS/q3_input.txt", "r")

data = f.readlines()

M = int(data[0])
data = data[1:]

apart = []

for i in data:
    row = list(map(int, filter(lambda x: x != "\n", i)))
    apart.append(row)

# 코드

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    global count
    count += 1
    apart[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < M) and (0 <= ny < M) and apart[nx][ny] == 1:
            dfs(nx, ny)


answer = []
for i in range(M):
    for j in range(M):
        count = 0
        if apart[i][j] == 1:
            dfs(i, j)

        if count != 0:
            answer.append(count)

for i in sorted(answer):
    print(i)

f.close()
end_time = time.time()
# print(end_time-start_time)
