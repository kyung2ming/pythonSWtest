# https://programmers.co.kr/learn/courses/30/lessons/60060 가사 검색
# test case
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]


def solution(words, queries):
    answer = []
    for q in queries:
        if q[0] == '?':
            answer.append(func2(words, q))
        else:
            answer.append(func1(words, q))
    return answer

def func1(words, q):
    words.sort()
    for i in range(len(q)):
        if q[i] == '?':
            break
    q1 = q[:i]
    start = 0
    end = len(words)
    mid = (start + end) // 2
    word = words[mid]
    if q1 < word[:i]:
        end = mid - 1

