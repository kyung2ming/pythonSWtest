# https://www.acmicpc.net/problem/10825
# 국영수
from sys import stdin

# (참고)파이썬 자료형 확인 : https://zetawiki.com/wiki/파이썬_자료형_확인_type()
def to_int(val):
    for i, info in enumerate(val):
        if i != 0:
            val[i] = int(info)

    return val


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    arr = [stdin.readline().strip().split(" ") for _ in range(N)]
    new_arr = list(map(to_int, arr))
    print(new_arr)

    # 파이썬 리스트 정렬 내장함수를 사용한다 : https://docs.python.org/3/howto/sorting.html
    # sort() 기존함수 변경, sorted() 정렬된 함수 반환 : https://cigiko.cafe24.com/python-정렬하기-sort와-sorted/
    # 파이썬 람다식 사용하기 : https://dojang.io/mod/page/view.php?id=2359, https://docs.python.org/3/howto/sorting.html
    # 다중정렬조건의 적용을 위해 람다식의 인자값을 튜플로 묶는다. 마이너스 부호를 더해 내림차순 정렬을 구현한다.
    new_arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

    for i in range(N):
        print(new_arr[i][0])