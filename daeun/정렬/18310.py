# https://www.acmicpc.net/problem/18310 안테나
import sys
N = int(input())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

print(li[(N-1)//2])