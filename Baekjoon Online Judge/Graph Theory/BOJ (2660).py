N=int(input())
graph=[[float('inf')]*N for _ in range(N)]
score=[0]*N

while True:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])  #각 친구들과의 최소단계 
            
for i in range(N):      
    for j in range(N):
        if i==j:
            continue
        score[i]=max(score[i],graph[i][j])    #자신과 가장 거리가 먼 친구와의 단계 계산
        
print(min(score),score.count(min(score)))     #회장 후보의 조건과, 만족하는 후보의 수 출력
print(" ".join(str(i+1) for i in range(N) if score[i]==min(score))) #회장 후보라면 번호 출력
