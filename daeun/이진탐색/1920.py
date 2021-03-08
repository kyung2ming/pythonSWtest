# https://www.acmicpc.net/problem/1920 수 찾기
import sys
n = int(input())
# set 자료형 이용
array = set(map(int, sys.stdin.readline().split()))

m = int(input())
x = list(map(int, sys.stdin.readline().split()))

for i in x:
    if i in array:
        print(1)
    else:
        print(0)
