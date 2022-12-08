import sys
input=sys.stdin.readline

n=int(input())
m=int(input())

MAX_VAL = 100001
graph=[[MAX_VAL]*n for _ in range(n)]

for _ in range(m):
    a,b,v = map(int,input().split())
    graph[a-1][b-1]=min(graph[a-1][b-1],v)
    
for i in range(n):
    graph[i][i]=0  
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(n):
    tmp = []
    for j in range(n):
        if graph[i][j]==MAX_VAL:
            tmp.append(0)
            continue
        tmp.append(graph[i][j])
    print(" ".join(map(str,tmp)))
            