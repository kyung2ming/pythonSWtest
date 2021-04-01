import sys

sys.stdin = open("q1_input.txt")

n = int(input())
mm = int(input())
g = [[sys.maxsize for _ in range(n+1)] for __ in range(n+1)]
for _ in range(mm):
    a, b, c = map(int, input().split())
    if g[a][b] == sys.maxsize or g[a][b] > c:
        g[a][b] = c


def Floyd_Warshall():
    for m in range(1, n+1):
        for s in range(1, n+1):
            for e in range(1, n+1):
                if g[s][e] > g[s][m] + g[m][e]:
                    g[s][e] = g[s][m] + g[m][e]


Floyd_Warshall()

for i in range(1, n+1):
    temp = ""
    for j in range(1, n+1):
        if j != 1:
            temp += " "

        if g[i][j] == sys.maxsize:
            temp += "0"
            continue

        if i == j:
            temp += "0"
        else:
            temp += str(g[i][j])
    print(temp)
