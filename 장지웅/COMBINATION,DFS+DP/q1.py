import sys
import math

sys.stdin = open("q1_input.txt")

n,m = map(int,input().split())

print(math.factorial(n)//math.factorial(n-m)//math.factorial(m))