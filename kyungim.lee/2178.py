# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# 파이썬의 다양한 입력방법 : https://velog.io/@tbnsok40/파이썬-다양한-입력방법-input-read-readline
from sys import stdin
from collections import deque

# dx[0], dy[0] => 오른쪽
# dx[1], dy[1] => 왼쪽
# dx[2], dy[2] => 아래
# dx[3], dy[3] => 위
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

if __name__ == '__main__':
    # https://velog.io/@pyh8618/Python-map-함수-사용법
    # 리스트의 요소를 지정된 함수로 처리한다. hashmap의 map이 아닌 mapping의 map이다

    # 첫 줄을 받아와 N, M 변수에 저장
    N, M = map(int, stdin.readline().split())

    # 이후의 데이터를 받아와 maze 배열에 저장
    # stdin.readline() : '101111\n'
    # stdin.readline().rstrip() : '101111'
    # M길이의 스트링을 N번 동적으로 넣어준다.
    # maze배열은 ['101111', '101010', '101011', '111011'] 형태의 1*4 배열이 되지만
    # 굳이 스트링을 split하지 않아도 maze[0][0] => '1' 과 같이 접근 가능하다
    # maze = [map(int, stdin.readline().rstrip()) for _ in range(N)]
    maze = [list(map(int, stdin.readline()[:-1])) for _ in range(N)]

    # 방문여부 배열
    # visited = [[False]*M for _ in range(N)]

    # BFS탐색을 위한 큐
    tmpQ = deque()

    # 변수 초기화
    tmpQ = [(0, 0, 1)]
    maze[0][0] = 0

    def bfs():
        # 0,0 에서부터 탐색 시작
        while tmpQ.__len__() > 0:
            curX, curY, cnt = tmpQ.pop()

            for i in range(4):
                nextX, nextY = curX + dx[i], curY + dy[i]

                # 정답인 경우
                if nextX == N - 1 and nextY == M - 1:
                    print(cnt+1)
                    return

                # 범위를 벗어나는 경우
                if nextX >= N or nextX < 0 or nextY >= M or nextY < 0:
                    continue

                # 이동할 수 없는 칸인경우(벽, 혹은 이미 방문한 칸)
                if maze[nextX][nextY] == 0:
                    continue

                # 지나온 칸은 벽으로 막는다
                maze[nextX][nextY] = 0
                tmpQ.append((nextX, nextY, cnt+1))

    bfs()