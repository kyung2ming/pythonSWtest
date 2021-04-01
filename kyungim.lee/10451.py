from sys import stdin

def dfs(i, graph, visited):

    nextI = graph[i]
    if not visited[nextI]:
        visited[nextI] = True
        dfs(nextI, graph, visited)
    else:
        return

if __name__ == '__main__':
    tc = int(stdin.readline())

    for _ in range(tc):
        k = int(stdin.readline())
        graph = [0] + list(map(int, stdin.readline().split()))
        visited = [False]*(k+1)
        tot = 0

        for i in range(1, k+1):
            # 순열의 시작
            if not visited[i]:
                tot += 1
                visited[i] = True
                dfs(i, graph, visited)

        print(tot)