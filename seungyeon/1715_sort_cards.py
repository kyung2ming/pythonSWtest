import sys
import heapq

# 최소 힙
sys.stdin = open("1715.txt", "rt")

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

sum = 0
heapq.heapify(arr)

while len(arr) > 1:
    first = heapq.heappop(arr)
    second = heapq.heappop(arr)
    sum += (first + second)
    heapq.heappush(arr, first + second)

print(sum)
