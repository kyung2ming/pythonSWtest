# 1707 이분그래프
from sys import stdin

K = map(int, stdin.readline())
color = [0]*22222
graph = [[] for _ in range(22222)]

def dfs(v):
    global color, graph, isBipartite
    reverseColor = 2 if color[v] == 1 else 1

    for val in graph[v]:

        # 연결된 정점이 아직 색칠되지 않았다
        if color[val] == 0:
            color[val] = reverseColor
            dfs(val)

        # 연결된 정점이 같은 색으로 색칠되었다 = 이분그래프 아님
        elif color[val] == color[v]:
            isBipartite = False

    return

if __name__ == '__main__':

    # 테스트 케이스는 총 K
    for _ in range(K):
        # V개의 정점과 E개의 간선을 가진 그래프
        V, E = map(int, stdin.readline().split())
        color = [0]*22222
        graph = [[] for _ in range(22222)]

        for _ in range(E):
            a, b = map(int, stdin.readline().split())
            graph[a].append(b)
            graph[b].append(a)

        # 그래프가 연결되지 않은 복수개 덩어리인 경우는 고려하지 않음 : 오류ㅠ 연결그래프 아닐 수 있다
        # print('YES') if dfs(1, color, graph) else print('NO')

        isBipartite = True
        for idx in range(1, V+1):
            # 아직 방문되지 않은 정점인 경우
            if color[idx] == 0:
                color[idx] = 1
                dfs(idx)

        print("YES") if isBipartite else print("NO")
