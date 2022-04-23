from sys import stdin
from collections import deque

N,M,K,X=map(int,stdin.readline().strip().split())
graph=[[]*(N+1) for _ in range(N+1)]
distance=[-1]*(N+1)
distance[X]=0

for i in range(M):
    a,b=map(int,stdin.readline().strip().split())
    graph[a].append(b)

dq=deque([X])   #bfs로 찾기 위해 queue선언 및 X와 연결된 간선부터 탐색 시작

while dq:
    now=dq.popleft()
    for node in graph[now]: #현재 node에 연결 되어 있는 node들을 확인
        if distance[node]==-1:  #연결되어 있는 노드가 이전에 탐색하지 않았던 곳이라면 
            distance[node]=distance[now]+1  #X에서 현재 node까지의 거리에 +1을 한 곳이 새로 발견한 곳의 최단 거리
            dq.append(node) #연결된 node를 deque에 삽입
if K not in distance:   #만약 distance에 K의 거리를 갖는 노드가 없다면 -1 출력
    print(-1)
else:
    for i in range(N+1):    #그렇지 않다면 오름차순으로 출력하기 위해 첫번째 노트부터 탐색
        if distance[i]==K:
            print(i)