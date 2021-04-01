# https://www.acmicpc.net/problem/10451 순열 사이클
# 11724번 참고
import sys
sys.setrecursionlimit(10000)  # 런타임 에러 방지
# 테스트케이스 개수
t = int(input())
result = []


def dfs(v):
    visit[v] = 1  # 방문처리
    for i in graph[v]:
        if visit[i] == 0:
            dfs(i)


while t > 0:
    t -= 1
    n = int(input())  # 순열의 크기
    array = list(map(int, sys.stdin.readline().split()))
    graph = [[] for i in range(n+1)]
    for i in range(1, n+1):
        j = array[i-1]
        graph[i].append(j)
        graph[j].append(i)
    visit = [0] * (n+1)
    count = 0
    for i in range(1, n + 1):
        if visit[i] == 0:
            dfs(i)
            count += 1
    result.append(count)

for i in result:
    print(i)





