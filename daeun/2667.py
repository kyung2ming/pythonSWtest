# 데이터 입력받기
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    global count
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return count
    return count


count_list = []
result = 0
for i in range(n):
    for j in range(n):
        count = 0
        if dfs(i, j):
            count_list.append(dfs(i, j))
            result += 1

# 오름차순 정렬
count_list.sort()
# 결과 출력
print(result)
for i in count_list:
    print(i)

