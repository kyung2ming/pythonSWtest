import sys
import bisect
import time

sys.stdin = open('BINARY/q1_input1.txt')

if __name__ == "__main__":

    n = int(input())
    a = [_ for _ in map(int, list(input().split()))]
    m = int(input())
    b = [_ for _ in map(int, list(input().split()))]

    a.sort()

    for bb in b:
        s, e = 0, len(a)-1
        while s <= e:
            mid = (e+s) // 2

            if a[mid] > bb:
                e = mid - 1
            elif a[mid] < bb:
                s = mid + 1
            else:
                break

        print(int(bb == a[mid]))

    # arr = [_ for _ in range(100000000)]
    # start = time.time()

    # for i in range(len(arr)):
    #     if 55555555 == arr[i]:  # 6.056549072265625
    #         break

    # s, e = 0, len(arr) # 0.003000020980834961
    # t = 55555555
    # while True:
    #     m = (e+s) // 2
    #     print(m)
    #     if m > t:
    #         e = m - 1
    #     elif m < t:
    #         s = m + 1
    #     else:
    #         break

    # 55555555 in arr  # 0.3749988079071045

    # end = time.time()
    # print(end - start)
