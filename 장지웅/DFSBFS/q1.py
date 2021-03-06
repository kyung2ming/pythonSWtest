import time
import sys
import path
import os
from collections import deque

# input.txt 가공
start_time = time.time()
f = open(os.getcwd() + "/DFSBFS/q1_input2.txt", "r")

data = f.readlines()

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

    # 스택 있는동안
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


# 수정필요 (숏코딩)
M, N = map(int, data[0].split('\n')[0].split())
box, ripe = [], deque()

for i in range(1, N+1):
    temp = []
    for j in data[i].strip().split():
        temp.append(int(j))
    box.append(temp)

# for i in range(N):
#     row = list(map(int, r().split()))
#     # for 1단계에서 띄어쓰기단위 무시
#     for j in range(M):
#         # for 2단계에서 띄어쓰기 체크
#         if row[j] == 1:
#             ripe.append([i, j])
#     box.append(row)
print(box)
print(bfs(M, N, box))
# 코드 끝

f.close()
end_time = time.time()
# print(end_time-start_time)
