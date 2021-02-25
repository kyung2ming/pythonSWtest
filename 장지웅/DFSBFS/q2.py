import time
import sys
import path
import os
from collections import deque

# input.txt 가공
start_time = time.time()
f = open(os.getcwd() + "/DFSBFS/q2_input.txt", "r")

data = f.readlines()

M, N = map(int, data[0].split())
data = data[1:]
maze, mov_maze = [], []
queue = deque()

for i in data:
    row = list(map(int, filter(lambda x: x != "\n", i)))
    maze.append(row)
    mov_maze.append(list(0 for _ in range(len(row))))

# 코드


def bfs(x, y):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue.append([0, 0])

    while queue:
        x, y = queue.popleft()
        print(x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < M) and (0 <= ny < N) and (maze[nx][ny] == 1):
                queue.append([nx, ny])
                maze[nx][ny] = maze[x][y] + 1

    return max(max(maze))


print(bfs(0, 0))

f.close()
end_time = time.time()
# print(end_time-start_time)
