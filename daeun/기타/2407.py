# https://www.acmicpc.net/problem/2407 조합
import sys
import math
n, m = map(int, sys.stdin.readline().split())
up = math.factorial(n)
down = (math.factorial(n-m)) * (math.factorial(m))
print(up // down)