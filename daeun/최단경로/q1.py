# https://programmers.co.kr/learn/courses/30/lessons/72413 합승 택시 요금
def solution(n, s, a, b, fares):
    INF = int(1e9)
    # 그래프 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    # 자기 자신으로 가는 비용은 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    m = len(fares)
    for i in range(m):
        a1 = fares[i][0]
        b1 = fares[i][1]
        c1 = fares[i][2]
        graph[a1][b1] = c1
        graph[b1][a1] = c1

    # 플로이드 알고리즘
    for k in range(1, n + 1):
        for a1 in range(1, n + 1):
            #  for b1 in range(1, n + 1): 시간초과
            for b1 in range(a1 + 1, n + 1):
                graph[a1][b1] = min(graph[a1][b1], graph[a1][k] + graph[k][b1])
                graph[b1][a1] = graph[a1][b1]

    cost = []
    # 경유지를 하나씩 지정해본다
    for mid in range(1, n + 1):
        cost.append(graph[s][mid] + graph[mid][a] + graph[mid][b])

    answer = min(cost)
    return answer
