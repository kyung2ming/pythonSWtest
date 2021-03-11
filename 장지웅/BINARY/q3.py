import bisect

def cus_bisect(arr,target):
    pass
#     if arr[bisect.bisect(arr, target) - 1] == target or arr[bisect.bisect(arr, target) - 1] == "?":
#         return arr[bisect.bisect(arr, target) - 1]
#     return None
    
def solution(words, queries):
    
    answer = []
    
    #words.sort()
    #print(words)
    for query in queries:
        count = 0
        len_query = len(query)
        for word in words:
            if len(word) == len_query:
                flag = True
                if query[0] == "?":
                    for alpha_idx in range(len(query)-1,0,-1):
                        if query[alpha_idx] == "?":
                            break
                        if query[alpha_idx] != word[alpha_idx]:
                            flag = False
                            break
                    if flag:
                        count += 1        
                else:
                    for alpha_idx in range(len(query)):
                        if query[alpha_idx] == "?":
                            break
                        if query[alpha_idx] != word[alpha_idx]:
                            flag = False
                            break
                    if flag:
                        count += 1          
        answer.append(count)
    
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))


'''
from bisect import bisect_left, bisect_right

def count_by_range(a, lv, rv):
    ri = bisect_right(a, rv)
    li = bisect_left(a, lv)
    return ri - li

def solution(words, queries):
    answer = []
    word_list = [[] for _ in range(10001)]
    reversed_word = [[] for _ in range(10001)]
    for word in words:
        word_list[len(word)].append(word)
        reversed_word[len(word)].append(word[::-1])
    
    for i in range(10001):
        word_list[i].sort()
        reversed_word[i].sort()
        
    for q in queries:
        if q[-1] == '?':
            res = count_by_range(word_list[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_by_range(reversed_word[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer

def solution(words, queries):
    word_list = [[] for _ in range(10001)]
    for word in words:
        word_list[len(word)].append(word)
    answer = []
    for query in queries:
        temp = 0
        q_list = query.split('?')
        q_left = q_list[0]
        q_right = q_list[-1]
        query_len = len(query)
        if q_left:
            q_len = len(q_left)
            for word in word_list[query_len]:
                if q_left == word[:q_len]:
                    temp+=1
        else:
            q_len = len(q_right)
            for word in word_list[query_len]:
                if q_right == word[-q_len:]:
                    temp+=1

        answer.append(temp)
    return answer
'''