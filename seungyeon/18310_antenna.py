import sys

sys.stdin = open("18310.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

if n % 2 == 0:
    compare = n // 2 - 1
else:
    compare = n // 2


print(arr[compare])
