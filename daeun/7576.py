from collections import deque

queue = deque()
# 데이터 입력받기
m, n = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 이동할 방향 (상, 하, 좌, 우)
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 구현
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])
bfs()
result = -2
# 안익은 토마토가 있는지 확인
flag = False

for i in graph:
    for j in i:
        if j == 0:
            flag = True
        result = max(result, j)

if flag:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)
