N,M=map(int,input().split())
money=[int(input()) for _ in range(N)]
dp=[10001]*(M+1)    #M은 최대 10000이고, 지폐의 최소단위가 1이므로 dp는 최대 10000 까지 가능하여 10001로 초기값 설정
dp[0]=0

for i in range(N):
    for k in range(money[i],M+1):
        if dp[k-money[i]]!=10001:   #만드는 것이 가능한 경우라면 update
            dp[k]=min(dp[k],dp[k-money[i]]+1)   #새로 갱신된 d[k-money[i]]+1이 기존에 저장된 d[k]보다 작다면 값 갱신
if dp[M]==10001:
    print(-1)
else:
    print(dp[M])