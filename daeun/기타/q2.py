# 다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.
#
# (), [], {} 는 모두 올바른 괄호 문자열입니다.
# 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
# 만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
# 대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# s의 길이는 1 이상 1,000 이하입니다.
# 입출력 예
# s	result
# "[](){}"	3
# "}]()[{"	2
# "[)(]"	0
# "}}}"	0

s = "[](){}"
def roll(s):
    s = s[1:] + s[0]
    print(s)
    return s


def isTrue(s):
    res = [0] * 3
    for i in s:
        if i == '(':
            res[0] += 1
        elif i == ')':
            res[0] -= 1
            if res[0] < 0:
                return False
        elif i == '{':
            res[1] += 1
        elif i == '}':
            res[1] -= 1
            if res[1] < 0:
                return False
        elif i == '[':
            res[2] += 1
        elif i == ']':
            res[2] -= 1
            if res[2] < 0:
                return False
    if sum(res) == 0:
        return True
    else:
        return False


def solution(s):
    answer = 0
    count = 0
    while count < len(s):
        count += 1
        if isTrue(s):
            answer += 1
        s = roll(s)

    return answer

print(solution(s))