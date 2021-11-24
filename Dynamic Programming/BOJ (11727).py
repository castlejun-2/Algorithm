N=int(input())
dp=[0,1,3]
for i in range(3,N+1):
    dp.append(dp[i-1]+dp[i-2]*2)
print(dp[N]%10007)

# N=1 => l (1가지)
# N=2 => ll , ㅁ, = (3가지)
# N=3 => lll, ㅁl, lㅁ, l=, =l (5가지)
# 2*N = 2*(N-1)에서 2*1 타일(l) 이 붙는 경우와 2*(N-2)에서 2*2 타일(ㅁ)과 2*1 타일(=)이 뒤에 붙는 경우가 더해지는 경우이므로
# dp[i] = dp[i-1] + dp[i-2]*2 의 점화식이 완성된다.
# 이 때 2*(N-2)의 경우 2*1이 아닌 1*2의 경우는 왜 넣지 않는지에 대해 의문일 수 있으나 이는 타일의 순서는 상관없이 조합만 뽑는 것이므로
# 1*2의 경우를 뽑을 경우 2*(N-2)의 경우에 중복됨으로 뽑아서는 안된다.
