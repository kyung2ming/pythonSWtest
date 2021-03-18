# https://www.acmicpc.net/problem/9251 LCS
arr1 = '0' + input()
arr2 = '0' + input()

n = len(arr1)
m = len(arr2)
d = [[0] * m for i in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if arr1[i] == arr2[j]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i][j-1], d[i-1][j])

print(d[n-1][m-1])
