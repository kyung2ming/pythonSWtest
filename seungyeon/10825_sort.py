import sys

sys.stdin = open("10825.txt", "rt")

n = int(input())
arr = []

for _ in range(n):
    # arr.append(tuple(input().split()))
    name, kor, eng, math = input().split()
    kor = int(kor)
    eng = int(eng)
    math = int(math)
    arr.append((name, kor, eng, math))

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(arr[i][0])
