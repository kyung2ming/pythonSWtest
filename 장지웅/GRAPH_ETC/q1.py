import sys

sys.stdin = open("q1_input2.txt")


def find_parent(x):

    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())  # <200
m = int(input())  # <1000

g = [[] for _ in range(n+1)]
board = [list(map(int, input().split())) for __ in range(n)]  # 최적화 가능
parent = [_ for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            # g[i+1].append(j+1)
            union_parent(i+1, j+1)

course = list(map(int, input().split()))

temp = parent[course[0]]

flag = 0

for i in course:
    if parent[i] != temp:
        flag = 1

if flag == 1:
    print("NO")
else:
    print("YES")
