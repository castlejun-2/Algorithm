from sys import stdin

N=int(stdin.readline())
increment_number_list=list(map(int,stdin.readline().split()))

dp=[0]*N
dp[0]=increment_number_list[0]

for i in range(1,N):
    temp_max=0
    for j in range(i):  #자신의 앞의 증가부분수열중 가장 큰 값을 temp_max에 저장 하여, 반복이 종료되면 해당 값을 증가수열의 i번째 index 값과 더해주어 저장한다.
        if increment_number_list[j] < increment_number_list[i]:
            temp_max=max(temp_max,dp[j])
    dp[i]=increment_number_list[i]+temp_max
print(max(dp))
