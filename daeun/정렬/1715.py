# https://www.acmicpc.net/problem/1715 카드 정렬하기
import heapq

N = int(input())
num = []
for i in range(N):
    num.append(int(input()))

num.sort()
result = 0
sum_list = []
if N == 1:
    result = num[0]
elif N == 2:
    result = num[0] + num[1]
else:
    sum_list.append(num.pop(0))
    while len(num) > 0:
        sum_list.append(sum_list[-1] + num.pop(0))
    sum_list.pop(0)
    result = sum(sum_list)

print(result)