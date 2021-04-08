import sys
import math

sys.stdin = open("q2_input.txt")

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    
    print(math.factorial(m)//math.factorial(m-n)//math.factorial(n))
    