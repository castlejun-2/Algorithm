N,M=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]

dp=[[0]*M for _ in range(N)]
dp[0][0]=graph[0][0]

for i in range(1,N):
    dp[i][0]=dp[i-1][0]+graph[i][0]

for i in range(1,M):
    dp[0][i]=dp[0][i-1]+graph[0][i]

for i in range(1,N):
    for j in range(1,M):
        dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+graph[i][j]  #올 수 있는 3곳의 위치에서 최대값을 갱신하며 자신에게 올 수 있도록 

print(dp[N-1][M-1])
