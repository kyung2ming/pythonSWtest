import sys

sys.stdin = open("1932.txt", "rt")

n = int(input())
dp = [0] * n
arr = [0] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i + 1):
        # 맨 처음
        if j == 0:
            arr[i][j] = arr[i][j] + arr[i - 1][j]
        # 맨 나중
        elif j == i:
            arr[i][j] = arr[i][j] + arr[i - 1][j - 1]
        else:
            arr[i][j] = arr[i][j] + max(arr[i - 1][j], arr[i - 1][j - 1])

print(max(arr[n - 1]))
