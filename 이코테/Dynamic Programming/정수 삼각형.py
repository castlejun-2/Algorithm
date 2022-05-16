n=int(input())
dp=[[0]*n for _ in range(n)]

dp[0][0]=int(input().strip())
for i in range(1,n):
    temp_list=list(map(int,input().strip().split()))
    dp[i][0]=dp[i-1][0]+temp_list[0]
    dp[i][i]=dp[i-1][i]+temp_list[-1]
    for j in range(1,i):
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+temp_list[j]
print(max(dp[-1]))