from collections import deque

def trace_route(dest):
    dq=deque([dest])
    
    while dq[0]!=N:                 #처음 위치를 만날 때 까지 이 전에 왔던 길을 추적
        dq.appendleft(route[dq[0]])
    
    return " ".join(map(str,dq))
    
def bfs(n):
    dq=deque([n])
    
    while dq: #거리를 bfs로 탐색
        x=dq.popleft()
        if x==K:  #도착지에 도달시 종료
            print(distance[K])
            print(trace_route(K))
            return
        for t in (x-1,x+1,x*2): 
            if 0<=t<=100000 and not distance[t]:  #값이 업데이트 되지 않았으며, 범위 이내의 값만 저장
                distance[t]=distance[x]+1
                route[t]=x  #자신이 이 전에 들린 위치 저장
                dq.append(t)

N,K=map(int,input().split())
distance=[0]*100001
route={}  #자신이 왔던길을 저장할 변수

bfs(N)
