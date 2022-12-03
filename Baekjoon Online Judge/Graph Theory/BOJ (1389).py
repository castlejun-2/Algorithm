N,M=map(int,input().split())
graph=[[0]*N for _ in range(N)]

for i in range(M):
    A,B=map(int,input().split())
    graph[A-1][B-1]=1
    grpah[B-1][A-1]=1
