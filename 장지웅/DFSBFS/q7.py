import time
import sys
from collections import deque

start_time = time.time()
sys.stdin = open("DFSBFS/q7_input1.txt", "r")

# 코드

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def calculation(count):
    global raw_board

    for c in range(1, count+1):
        temp_sum = 0
        temp_count = 0

        q = deque()

        for i in range(n):
            for j in range(n):
                if boarder[i][j] == c:
                    q.append([i, j])
                    temp_sum += raw_board[i][j]
                    temp_count += 1

        while q:
            i, j = q.popleft()
            raw_board[i][j] = temp_sum // temp_count


def bfs(x, y, count):
    board = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            board[i][j] = raw_board[i][j]

    q = deque()
    q.append([x, y])
    boarder[x][y] = count
    temp_flag = False
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and (l <= abs(board[x][y]-board[nx][ny]) <= r) and not boarder[nx][ny]:
                q.append([nx, ny])
                temp_flag = True
                boarder[nx][ny] = count

    return temp_flag


if __name__ == "__main__":
    n, l, r = map(int, input().split())

    raw_board = [list(map(int, input().split())) for _ in range(n)]

    answer = 0

    while True:
        flag = False
        boarder = [[0 for _ in range(n)] for _ in range(n)]
        count = 0
        for k in range(n):
            for m in range(n):
                if not boarder[k][m]:
                    count += 1
                    flag += bfs(k, m, count)

        if flag == False:
            print(answer)
            break

        else:
            answer += 1
            calculation(count)

end_time = time.time()
# print(end_time-start_time)
