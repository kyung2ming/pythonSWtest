# https://www.acmicpc.net/problem/18352
# 특정 거리의 도시 찾기
from sys import stdin
from collections import deque

if __name__ == "__main__":
    # 도시의 개수, 도로의 개수, 거리정보, 출발 도시의 번호
    N, M, K, X = map(int, stdin.readline().strip().split(" "))

    # 목적지 정보 배열 선언
    arr = [[] for _ in range(N+1)]

    # 최소경로 길이정보 배열 선언
    min_len = [0 for _ in range(N+1)]

    # M개의 도시에 대한 A -> B 단방향 경로정보를 입력받는다.
    for _ in range(M):
        A, B = map(int, stdin.readline().strip().split(" "))
        arr[A].append(B)

    # X에서 갈 수 있는 목적지 b들을 큐에 넣는다
    res = []
    tmpQ = deque()

    for b in arr[X]:
        tmpQ.append((b, 1))
        min_len[b] = 1
    # map(tmpQ.append((x, 1)), arr[X])
    # (tmpQ.append((b, 1)) for b in arr[X])

    while True:
        if tmpQ.__len__() <= 0:
            break

        # 다음 목적지의 정보를 받는다
        curB, kCnt = tmpQ.popleft()

        # K번 초과한 경우
        if kCnt > K:
            break

        # K번 도달한 경우
        if kCnt == K:
            if min_len[curB] == 0 or min_len[curB] >= kCnt:
                print(curB)
                min_len[curB] = kCnt
        # K번 도달 가능한 경로가 없는경우
        elif kCnt < K and tmpQ.__len__() <= 0:
            print("-1")
            break
        else:
            for nextB in arr[curB]:
                tmpQ.append((nextB, kCnt+1))

