n=int(input())
dp=[[0]*n for _ in range(n)]

dp[0][0]=int(input().strip())
for i in range(1,n):
    temp_list=list(map(int,input().strip().split()))
    dp[i][0]=dp[i-1][0]+temp_list[0]    #삼각형의 가장 앞은 그 위의 삼각형 가장 앞의 값만 이어 받을 수 있다.
    for j in range(1,i+1):
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+temp_list[j]  #그 외의 값들은 대각선의 값을 참고하며, 마지막 값은 그 위의 값이 0이므로 그대로 참고한다.
print(max(dp[-1]))  #마지막 삼각형의 값들중 최대값을 출력한다.