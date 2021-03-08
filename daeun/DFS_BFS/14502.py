# https://www.acmicpc.net/problem/14502 연구소
# pypy3로 제출

import sys
n, m = map(int, input().split())
s = []  # 초기 리스트
for i in range(n):
    s.append(list(map(int, input().split())))
# s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

max_result = 0


# 바이러스를 퍼뜨리기
def bfs():
    global max_result
    # copy = copy.deepcopy(s)
    # 리스트를 그대로 복사
    copy = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            copy[i][j] = s[i][j]
    result = 0
    arr = []
    for i in range(n):
        for j in range(m):
            if copy[i][j] == 2:
                arr.append([i, j])
    while arr:
        a, b = arr[0][0], arr[0][1]
        del arr[0]
        for i in range(4):
            ax = a + dx[i]
            ay = b + dy[i]
            if 0 <= ax < n and 0 <= ay < m:
                if copy[ax][ay] == 0:
                    copy[ax][ay] = 2
                    arr.append([ax, ay])

    # 안전구역 크기 계산
    for i in copy:
        for j in i:
            if j == 0:
                result += 1
    max_result = max(max_result, result)  # 큰 값 저장


# 벽 세우기
def wall(count):
    if count == 3:  # 벽을 3개 설치한 경우
        bfs()  # bfs 실행
        return
    for i in range(n):
        for j in range(m):
            if s[i][j] == 0:
                s[i][j] = 1
                count += 1
                wall(count)
                s[i][j] = 0


wall(0)
print(max_result - )