import sys

def floyd(n,g):
    for m in range(1, n+1):
        for s in range(1, n+1):
            for e in range(1,n+1):
                if g[s][e] > g[s][m] + g[m][e]:
                    g[s][e] = g[s][m] + g[m][e]
    
    
def solution(n, results):
    
    g = [[sys.maxsize for _ in range(n+1)] for __ in range(n+1)]

    for i in results:
        g[i[0]][i[1]] = 1
    
    floyd(n,g)
    
    answer = 0
    
    for i in range(1,len(g)):
        flag = 1
        for j in range(1,len(g)):
            
            if i != j and g[i][j] == sys.maxsize and g[j][i] == sys.maxsize:
                flag = 0
                break

        if flag == 1:
            answer += 1
            
    # for i in range(1,n+1):
    #     print(g[i][1:])
    
    
    return answer