from sys import stdin
from collections import deque

N,K=map(int,stdin.readline().split())
distance=[-1]*100001

def bfs(n):
    dq=deque([n])
    distance[n]=0
    cnt=0
    
    while dq:
        val=dq.popleft()
    
        if val==K:    #목적지에 도착 했다면 최소경로로 도착한 것이므로 +1
            cnt+=1
        else:
            for t in (val-1,val+1,val*2):
                if 0<=t<=100000 and (distance[t]==-1 or distance[t]==distance[val]+1):  #앞에서 개척한 거리와 같거나 아직 도착하지 않은 경로이면
                    distance[t]=distance[val]+1                                         #경로 업데이트
                    dq.append(t)
    return cnt  

count=bfs(N)    
print(distance[K])
print(count)
