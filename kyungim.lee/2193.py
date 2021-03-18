# Baekjoon 2193 이친수
# DP문제
from sys import stdin

def solve(idx):
    
    if idx == 1 or idx == 2:
        return 1
    
    # ret 변경시에 memo[idx] 내용도 변경
    # c++ 코드에서는 alias로 받아온다 (ex) int &ret = memo[idx];
    ret = memo[idx]
    if ret != -1:
        return ret

    ret = solve(idx-1) + solve(idx-2)
    memo[idx] = ret
    
    return ret

if __name__ == '__main__':

    # N자리 이친수의 개수를 찾는다
    N = 65

    # memoization N+1크기 배열 선언
    memo = [-1 for _ in range(N+1)]

    # 점화식 x(n) = x(n-1) + x(n-2)
    print(solve(N))