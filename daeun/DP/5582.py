# https://www.acmicpc.net/problem/5582 공통 부분 문자열
arr1 = '0' + input()
arr2 = '0' + input()

n = len(arr1)
m = len(arr2)
d = [[0] * m for i in range(n)]

result = 0

for i in range(1, n):
    for j in range(1, m):
        if arr1[i] == arr2[j]:
            d[i][j] = d[i-1][j-1] + 1
            result = max(result, d[i][j])

print(result)
