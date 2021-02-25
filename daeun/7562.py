from collections import deque

# 이동할 방향
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


# BFS
def bfs(so_x, so_y, de_x, de_y):
    queue = deque()
    queue.append([so_x, so_y])
    graph[so_x][so_y] = 1
    while queue:
        a, b = queue.popleft()
        if a == de_x and b == de_y:
            print(graph[de_x][de_y] - 1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and graph[x][y] == 0:
                queue.append([x, y])
                graph[x][y] = graph[a][b] + 1


num = int(input())  # 테스트 케이스의 개수
for i in range(num):
    n = int(input())  # 체스판 한 변의 길이
    so_x, so_y = map(int, input().split())  # sorce
    de_x, de_y = map(int, input().split())  # destination
    graph = [[0] * n for i in range(n)]
    bfs(so_x, so_y, de_x, de_y)
