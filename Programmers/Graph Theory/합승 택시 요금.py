import heapq

def solution(n, s, a, b, fares):
    def dijkstra(start, end):         #start에서 end까지의 최소값 반환
        if start == end:
            return 0
        q = []
        heapq.heappush(q,(0,start-1))
        distance = [1e9]*n
        distance[start-1] = 0
        
        while q:
            dis,idx=heapq.heappop(q)
            
            if distance[idx] < dis:
                continue
            
            for i in _dict[idx]:
                if graph[idx][i] + dis < distance[i]:
                    distance[i]=graph[idx][i]+dis
                    heapq.heappush(q,(distance[i],i))
                    
        return distance[end-1]
    
    graph = [[1e9]*n for _ in range(n)]
    _dict = { i: [] for i in range(n)}
    
    for fare in fares:
        c,d,f=fare[0]-1,fare[1]-1,fare[2]
        graph[c][d]=f
        graph[d][c]=f
        _dict[c].append(d)
        _dict[d].append(c)
    
    for i in range(n):  #i에서 i로 가는 거리 0으로 설정
        graph[i][i]=0
    
    answer = 1e9
    
    for i in range(1,n+1):  #각 노드를 함께 경유할 때의 최소값을 갱신한다.
        answer = min(answer,dijkstra(s,i)+dijkstra(i,a)+dijkstra(i,b))
    return answer
