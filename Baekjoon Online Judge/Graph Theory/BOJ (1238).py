import heapq

MAX_VAL = 1e9

N,M,X=map(int,input().split())
graph=[[MAX_VAL]*N for _ in range(N)]
_dict={i:[] for i in range(N)}
answer=0

for _ in range(M):
    s,e,v=map(int,input().split())
    graph[s-1][e-1]=v
    _dict[s-1].append(e-1)

_q = []
heapq.heappush(_q,(0,X-1))
dist = [MAX_VAL]*N
dist[X-1] = 0

while _q:
    dis,idx = heapq.heappop(_q)
        
    if dist[idx] < dis or dist[idx]!=MAX_VAL:
        continue
        
    for k in _dict[idx]:
        if dis+graph[idx][k] < dist[k]:
            dist[k]=dis+graph[idx][k]
            heapq.heappush(_q,(dist[k],k))

for i in range(N):
    if i==X-1:
        continue
    q = []
    heapq.heappush(q,(0,i))
    distance = [MAX_VAL]*N
    distance[i] = 0
    
    while q:
        dis,idx = heapq.heappop(q)
        
        if distance[idx] < dis or distance[idx]!=MAX_VAL:
            continue
        
        for k in _dict[idx]:
            if dis+graph[idx][k] < distance[k]:
                distance[k]=dis+graph[idx][k]
                heapq.heappush(q,(distance[k],k))
                
    answer=max(answer,distance[X-1]+dist[i])
print(answer)