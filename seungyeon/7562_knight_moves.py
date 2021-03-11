import sys
from collections import deque

sys.stdin = open("7562.txt", "rt")

def bfs(now_x,now_y, dest_x, dest_y):
    q =deque()
    q.append((now_x,now_y))
    visited[now_x][now_y] = 1
    while q:
        x, y = q.popleft()
        if x == dest_x and y == dest_y:
            print(visited[dest_x][dest_y] -1)
            break
        for i in range(8):
            if not (0<= x + dx[i] <= n-1):
                continue
            if not (0<= y + dy[i] <= n-1):
                continue
            if visited[x+dx[i]][y+dy[i]] == 0:
                visited[x+dx[i]][y+dy[i]] = 1
                q.append((x+dx[i], y+dy[i]))
                visited[x+dx[i]][y+dy[i]] = visited[x][y] + 1



if __name__ == "__main__":
    count = int(input())
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    for i in range(count):
        n = int(input())
        visited = [[0]*n for _ in range(n)]
        now_x, now_y = map(int, input().split())
        dest_x, dest_y = map(int, input().split())
        bfs(now_x,now_y, dest_x, dest_y)




