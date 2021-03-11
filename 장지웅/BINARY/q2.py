import sys
import time

sys.stdin = open('BINARY/q2_input2.txt')


def binary(m, arr):  # m = 가져가야 할 목재
    start, end = 0, sum(arr)

    while start <= end:

        mid = (start+end) // 2
        temp_sum = 0
        for i in arr:
            if i > mid:
                temp_sum += i - mid

        if temp_sum > m:  # 조건문을 변형 가능
            start = mid + 1
        elif temp_sum < m:
            end = mid - 1
        else:
            break
    return mid


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [_ for _ in map(int, input().split())]

    print(binary(m, arr))
