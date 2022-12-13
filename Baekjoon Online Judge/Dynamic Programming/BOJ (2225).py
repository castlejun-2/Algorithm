N,K=map(int,input().split())
dp=[[0]*(N+1) for _ in range(K)]

for i in range(N+1):    #1개로 N을 만드는 방법은 모두 1이다.
    dp[0][i]=1  
    
for i in range(1,K):
    for j in range(N+1):
        for k in range(0,j+1):
            dp[i][j]+=dp[i-1][k]    #k개로 N을 만드는 방법은 K-1개로 N을 만드는 방법에 +0, K-1개로 N-1을 만드는 방법에 +1 ... 가능하다.

print(dp[-1][-1]%1000000000)    #K개로 N을 만드는 방법을 출력한다.