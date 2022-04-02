n,k = map(int,input().split())
c_list = [int(input()) for _ in range(n)]
dp = [1]+[0]*k

for coin in c_list:
    for i in range(1,k+1):
        if i-coin>=0:
            dp[i]+=dp[i-coin]         #dp[i-coin]은 dp[4]에 대한 값을 계산한다고 할 때 만약 현재 선택된 coin이 2라면 이 전에 누적된 방법의 합인 dp[4]에
                                      #dp[4-2]를 더한값이다. 즉 dp[4-2]는 현재로부터 2 coin의 값어치를 뺀 dp[2] 즉 dp[2]는 2원의 합을 도출하는 누적값인데
print(dp[k])                          #이 값의 모든 경우의수에 +2(현재 선택된 코인의 값어치)를 더해주면 새로운 방법이 도출되므로 dp[i]=dp[i]+dp[i-coin]의 식이 성립한다.
