import sys

sys.stdin = open("1920.txt", "rt")


def binary_search(A, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == target:
            print(1)
            return
        elif A[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    print(0)
    return


n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
arr = list(map(int, input().split()))

for x in arr:
    binary_search(A, x, 0, n - 1)
