MAX_VAL = 1e9

n,m,r=map(int,input().split())
item = list(map(int,input().split()))
graph = [[MAX_VAL]*n for _ in range(n)]
answer = 0

for _ in range(r):
    a,b,l=map(int,input().split())
    graph[a-1][b-1]=l
    graph[b-1][a-1]=l

for i in range(n):
    graph[i][i]=0    
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    
for i in range(n):
    items = 0
    for j in range(n):
        if graph[i][j] <= m:
            items += item[j]
    answer = max(answer,items)

print(graph)

print(answer)