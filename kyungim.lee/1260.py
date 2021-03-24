from collections import deque
from sys import stdin

tmpQ = deque()
visited = [0] * 1111

# 그래프 이름을 map으로 하면 map() 함수와 충돌나서 list object is not callable 오류 발생한
graph = [[0] * 1111 for _ in range(1111)]

def dfs(a):
    global graph, visited

    # a와 연결된 모든 간선에 대해 탐색한다
    for idx, val in enumerate(graph[a]):

        # 간선이 연결되어 있고 아직 방문하지 않은 정점인 경우
        if val == 1 and visited[idx] == 0:
            print(idx, end=' ')
            visited[idx] = 1
            dfs(idx)

    return


def bfs(root):
    global graph, visited

    for idx, val in enumerate(graph[root]):

        if val == 1:
            tmpQ.append(idx)

    # print(tmpQ)

    while (True):

        if tmpQ.__len__() == 0:
            break;

        curIdx = tmpQ.popleft()

        if visited[curIdx] == 0:
            print(curIdx, end=' ')
            visited[curIdx] = 1

            for idx, val in enumerate(graph[curIdx]):

                if val == 1 and visited[idx] == 0:
                    tmpQ.append(idx)

    return

def init():
    # global 전역변수로 지정해주지 않으면 함수 내에서 전역변수의 값에 접근불가
    # 동일한 이름의 지역변수로 선언된다 : https://dojang.io/mod/page/view.php?id=2364
    global visited

    visited = [0] * 1111
    visited[V] = 1

    # print시 줄바꿈 아닌 원하는 문자 출력한다
    print(V, end=' ')

if __name__ == '__main__':

    N, M, V = map(int, stdin.readline().split())

    for _ in range(M):
        a, b = map(int, stdin.readline().split())

        # 간선을 입력받아 표시한다. 연결되어있으면 1
        graph[a][b] = 1
        graph[b][a] = 1

    init()
    dfs(V)
    print('')

    init()
    bfs(V)