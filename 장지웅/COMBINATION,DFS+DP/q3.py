import sys
import time

sys.stdin = open("q3_input.txt")

m, n = map(int, input().split())  # 가로5, 세로4

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    ###############
    # DFS 상단부
    if x == m - 1 and y == n - 1:  # x,y가 최종 목적지일 경우 최초 카운트
        return 1
    if count[x][y] != -1:  # dp 조건문을 실행할 경우 시간절약
        return count[x][y]
    count[x][y] = 0  # 방문 체크
    ###############

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if board[nx][ny] < board[x][y]:
                ###############
                # nx,ny 지점
                count[x][y] += dfs(nx, ny)  # count[x][y] 누적합
                ###############
    ###############
    # return 지점
    return count[x][y]  # nonetype을 리턴하지 않게 함
    ###############


board = [list(map(int, input().split())) for _ in range(m)]  # board[5][4]
count = [[-1 for __ in range(n)] for _ in range(m)]


dfs(0, 0)

print(count[0][0])
