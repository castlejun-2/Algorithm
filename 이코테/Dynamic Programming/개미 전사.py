N=int(input())
house=list(map(int,input().split()))

dp=[0]*(N)
dp[0]=house[0]
dp[1]=max(house[0],house[1])

for i in range(2,N):    #이 전의 식량을 털면 현재 위치의 식량을 털 수 없으므로, 두가지 선택 중 큰 값을 선택
    dp[i]=max(dp[i-1],dp[i-2]+house[i])
    
print(dp[N-1])