N,M=map(int,input().split())
graph=[[float('inf')]*N for _ in range(N)]
answer=[0]*N

for i in range(M):
    A,B=map(int,input().split())
    graph[A-1][B-1]=1
    graph[B-1][A-1]=1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])    #연결되어 있는 친구의 최솟값 탐색

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        answer[i]+=graph[i][j]      #자기 자신을 제외한 케빈 베이컨 법칙의 합 계산

print(answer.index(min(answer))+1)  #최소값을 갖는 index 중 가장 앞의 값 반환
