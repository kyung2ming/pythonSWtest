import sys
import heapq

def dijkstra(n,fares,start, end):
    
    g = [[] for _ in range(n+1)]
    distance = [sys.maxsize] * (n+1)
    
    for i in fares:
        g[i[0]].append([i[1],i[2]])
        g[i[1]].append([i[0],i[2]])
    
    q = []
    heapq.heappush(q,[0,start])
    
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in g[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,[cost,i[0]])

    return distance[end]
    
                
    
def solution(n, s, a, b, fares):
    
    answer = sys.maxsize
    
    for i in range(1,n+1):
        if dijkstra(n,fares,a,s) == sys.maxsize or dijkstra(n,fares,b,s) == sys.maxsize:
            continue
        answer = min(answer,dijkstra(n,fares,a,i)+ dijkstra(n,fares,b,i)+ dijkstra(n,fares,s,i))
    
    return answer