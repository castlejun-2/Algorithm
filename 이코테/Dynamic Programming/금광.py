import numpy
import copy

move=[(-1,1),(0,1),(1,1)]
T=int(input())

for i in range(T):
    n,m=map(int,input().strip().split())
    gold_list=numpy.array(list(map(int,input().strip().split())))
    gold_list=gold_list.reshape(n,m)
    dp=copy.deepcopy(gold_list)
    
    for j in range(n):
        for k in range(m):
            for t in range(3):
                nx=j+move[t][0]
                ny=k+move[t][1]
                if 0<=nx<n and 0<=ny<m:
                    dp[nx][ny]=max(dp[nx][ny],dp[j][k]+gold_list[nx][ny])
                    print("j,k",j,k,"dp[j][k]",dp[j][k],"nx,ny: ",nx,ny,"dp[nx][ny]: ",dp[nx][ny], "dp[j][k]+gold_list[nx][ny]: ",dp[j][k]+gold_list[nx][ny])
    answer=dp[0][m-1]
    for j in range(n):
        answer=max(answer,dp[j][m-1])
    print(answer)