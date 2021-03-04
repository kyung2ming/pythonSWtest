import sys

sys.stdin = open("SORT/q1_input.txt", "r")

if __name__ == "__main__":
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

    for i in arr:
        print(i[0])
