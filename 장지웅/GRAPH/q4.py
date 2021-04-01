import sys

sys.stdin = open("q4_input.txt")

t = int(input())


def dfs(n):

    visited[n] = 1

    if not visited[g[n]]:
        dfs(g[n])

    return 1


for _ in range(t):

    n = int(input())

    g = [0 for __ in range(n+1)]
    li = list(map(int, input().split()))
    visited = [0 for __ in range(n+1)]

    for i in range(1, n+1):
        g[i] = li[i-1]

    answer = 0

    for i in range(1, n+1):
        if not visited[i]:
            answer += dfs(i)
    print(answer)
