N=int(input())
number_list=list(map(int,input().split()))

dp=[1]*N

for i in range(1,N):
    temp_max=1
    for j in range(i):  #자신보다 앞에 있는 감소하는 수열중에서, 자신보다 작은 큰 값을 만나면 수열이 증가하는 것이므로
        if number_list[i]<number_list[j]:
            temp_max=max(temp_max,dp[j]+1)
    dp[i]=temp_max  #해당 수열 중에서 자신이 추가되어 +1이 되었을 때, 가장 큰 값을 dp[i]에 저장하여준다.

print(dp[N-1])