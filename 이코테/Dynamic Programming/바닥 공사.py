N=int(input())

dp=[0]*N
dp[0]=1
dp[1]=3 #1*2 2개, 2*1 2개, 2*2 1개

for i in range(2,N):    #dp[i-1]에 2*1의 타일을 붙히는 경우와 dp[i-2]에 2*2, 1*2를 2개 붙히는 경우가 존재한다.
    dp[i]=(dp[i-1]+dp[i-2]*2)%796796

print(dp[N-1])