# import sys
# import heapq
# sys.stdin = open("test_input.txt")

# n = int(input())

# q = []

# for _ in range(n):
#     temp = int(input())

#     if temp == 0:
#         if len(q) == 0:
#             print(0)
#         else:
#             print(heapq.heappop(q))
#     else:
#         heapq.heappush(q, temp)

import sys
import heapq

n = int(sys.stdin.readline())

q = []

for _ in range(n):
    temp = int(input())

    if temp == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, temp)
