import sys

sys.stdin = open('DYNAMIC/q3_input.txt')

if __name__ == "__main__":
    n = int(input())

    arr = [list(map(int,input().split())) for _ in range(n)]

    for i in range(n-2,-1,-1):
        for j in range(i+1):
            arr[i][j] += max(arr[i+1][j],arr[i+1][j+1])

    print(arr[0][0])