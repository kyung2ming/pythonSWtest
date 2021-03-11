import sys

sys.stdin = open("2805.txt", "rt")


def binary_search(arr, start, end):
    res = 0
    while start <= end:
        trees = 0
        mid = (start + end) // 2

        for x in arr:
            if x > mid:
                trees += (x - mid)
        if trees < m:
            end = mid - 1
        else:
            res = mid
            start = mid + 1

    return res


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = binary_search(arr, 0, arr[n - 1])
print(result)
