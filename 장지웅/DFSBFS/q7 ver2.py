import time
import sys
from collections import deque

start_time = time.time()
sys.stdin = open("DFSBFS/q7_input4.txt", "r")

# 코드

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y, count):

    q = deque()
    q.append([x, y])
    boarder[x][y] = count
    temp_sum = board[x][y]
    temp_count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and (l <= abs(board[x][y]-board[nx][ny]) <= r) and not boarder[nx][ny]:
                q.append([nx, ny])
                temp_sum += board[nx][ny]
                temp_count += 1
                boarder[nx][ny] = count
    print(board, boarder)
    if temp_count >= 2:
        return temp_sum // temp_count
    else:
        return 0


if __name__ == "__main__":
    n, l, r = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]

    answer = 0

    while True:
        flag = False
        boarder = [[0 for _ in range(n)] for _ in range(n)]
        count = 0
        temp = 0
        for k in range(n):
            for m in range(n):
                if not boarder[k][m]:
                    count += 1
                    temp += bfs(k, m, count)
                    # print(temp)
                    if temp != 0:
                        answer += 1
                        for i in range(n):
                            for j in range(n):
                                if boarder[i][j] == count:
                                    board[i][j] = temp
                        flag = True

        if flag == False:
            print(answer)
            break


end_time = time.time()
# print(end_time-start_time)
