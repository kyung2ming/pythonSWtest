import sys

sys.stdin = open('q7_input.txt')

n = int(input())

arr = list(map(int, input().split()))

dp1 = [0] * n
dp2 = [0] * n

for i in range(n):
    dp1[i] = 1
    for j in range(i):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

arr = list(reversed(arr))

for i in range(n):
    dp2[i] = 1
    for j in range(i):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

dp3 = [dp1+dp2 for dp1, dp2 in zip(dp1, dp2)]

print(dp3)
