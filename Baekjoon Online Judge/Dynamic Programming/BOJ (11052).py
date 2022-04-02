N = int(input())
c_list = [0]+list(map(int,input().split()))

dp = [0]*(N+1)            #for문에서 dp[N]을 비교해야 하므로, 미리 0으로 초기화하여 선언
dp[1] = c_list[1]         #1장만 뽑을 때는 무조권 c_list[1]이 최댓값이 된다.
  
for i in range(2,N+1):
    for j in range(1,i+1):
        # 카드의 갯수를 K라고 할 때 K-1번째까지의 최대값에서 1번째를 더하는 경우, K-2번째까지의 최대값에서 2번째를 더하는 경우등을 비교해 나아가면서 최대값을 결정 
        if dp[i] < dp[i-j]+c_list[j]:
            dp[i] = dp[i-j]+c_list[j]

print(dp[N])
