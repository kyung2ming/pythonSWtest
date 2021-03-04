# https://www.acmicpc.net/problem/10825 국영수
import sys

# 데이터 입력받기
N = int(input())
student_list = [list(sys.stdin.readline().split()) for _ in range(N)]

student_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in student_list:
    print(str(student[0]))
