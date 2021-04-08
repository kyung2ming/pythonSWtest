# https://www.acmicpc.net/problem/1010 다리 놓기
import sys
import math

num = int(input())
result = []
for i in range(num):
    m, n = map(int, sys.stdin.readline().split())
    up = math.factorial(n)
    down = (math.factorial(n-m)) * (math.factorial(m))
    result.append(up // down)

for i in result:
    print(i)