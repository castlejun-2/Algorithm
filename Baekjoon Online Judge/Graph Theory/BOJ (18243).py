N,K=map(int,input().split())

graph=[[float('inf')]*N for _ in range(N)]
answer=True

for _ in range(K):
    A,B=map(int,input().split())
    graph[A-1][B-1]=1
    graph[B-1][A-1]=1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])  #각 노드의 최단거리를 탐색한다.

for i in range(N):
    _relation=0
    for j in range(N):
        if i==j:
            continue
        _relation=max(_relation,graph[i][j])
    if _relation > 6:   #6단계를 넘어서 알게되는 친구가 존재한다면 세상은 너무 크다.
        answer=False
        break
if answer:
    print("Small World!")
else:
    print("Big World!")
