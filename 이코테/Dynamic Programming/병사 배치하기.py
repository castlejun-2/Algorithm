N=int(input())
solider=list(map(int,input().strip().split()))
dp=[1]*N

for i in range(N):
    for j in range(i):
        if solider[i] < solider[j]:
            dp[i]=max(dp[i],dp[j]+1)    #앞에서 부터 가장 긴 감소하는 수열을 만든다

print(N-max(dp))    #총 배열의 길이에서 가장 긴 감소하는 수열의 길이를 빼면 최소 열외인원을 알 수 있다.