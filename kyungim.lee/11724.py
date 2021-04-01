from sys import stdin
from collections import deque

# 인접리스트로 구현한다. 그냥 1차원 리스트로 선언하면 graph[v].append()사용불가
graph = [[] for _ in range(1111)]
visited = [0]*1111

# 재귀함수의 파라미터로 맵을 넘기는것과 전역키워드 설정하는 것 중에 뭐가 더 좋은지?
# 파라미터로 넘길때 포인터로 넘겨서 상관없으려나..
def dfs(v):
    global visited, graph

    # 해당 정점과 연결된 모든 정점을 방문한다
    for curV in graph[v]:

        # 방문한 적 없는 정점인경우 방문
        if visited[curV] == 0:
            visited[curV] = 1
            dfs(curV)

if __name__ == '__main__':
    ret = 0
    N, M = map(int, stdin.readline().split())

    for _ in range(M):
        u, v = map(int, stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    # range(start, end) : start 이상 end 미만
    for val in range(1, N+1):

        # 방문한 적 없는 정점인 경우 해당 정점과 연결된 모든 정점을 방문한다
        if visited[val] == 0:
            ret += 1
            visited[val] = 1
            dfs(val)

    print(ret)