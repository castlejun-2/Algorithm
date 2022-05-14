import numpy
import copy

move=[(-1,1),(0,1),(1,1)]
T=int(input())

for i in range(T):
    n,m=map(int,input().strip().split())
    gold_list=numpy.array(list(map(int,input().strip().split())))
    gold_list=gold_list.reshape(n,m)
    dp=copy.deepcopy(gold_list)
    
    for col in range(m):    #한 열부터 조사를 시작
        for j in range(n):  #열의 각 행들의 현재까지의 최대값을 저장
            for t in range(3):  #이동 가능한 방향 조사
                nx=j+move[t][0]
                ny=col+move[t][1]
                if 0<=nx<n and 0<=ny<m:
                    dp[nx][ny]=max(dp[nx][ny],dp[j][col]+gold_list[nx][ny])
    answer=dp[0][m-1]   #마지막 열에 저장된 최댓값을 결과값에 저장
    for j in range(1,n):    
        answer=max(answer,dp[j][m-1])   
    print(answer)