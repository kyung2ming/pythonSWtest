import time
import sys
from collections import deque


start_time = time.time()
sys.stdin = open("DFSBFS/q6_input3.txt", "r")

# 코드

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs():
    global safety_area
    board = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            board[i][j] = raw_board[i][j]

    queue = deque()

    for k in range(n):
        for l in range(m):
            if raw_board[k][l] == 2:
                queue.append([k, l])
    while queue:
        x, y = queue.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and (board[nx][ny] == 0):
                queue.append([nx, ny])
                board[nx][ny] = 2
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count += 1

    safety_area = max(safety_area, count)


def wall(x):
    if x == 3:
        bfs()
        return
    for k in range(n):
        for l in range(m):
            if raw_board[k][l] == 0:
                raw_board[k][l] = 1
                wall(x+1)
                raw_board[k][l] = 0


if __name__ == "__main__":

    n, m = map(int, input().split())
    raw_board = [list(map(int, input().split())) for _ in range(n)]

    safety_area = 0
    wall(0)

    print(safety_area)

end_time = time.time()
# print(end_time-start_time)
