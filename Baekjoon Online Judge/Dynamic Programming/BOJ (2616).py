N=int(input())
train_list=list(map(int,input().split()))
T=int(input())

particle_sum=[0]
val=0

for train in train_list:    #부분합을 통해 각 객차를 선택했을 때의 승객 합을 계산
    val+=train
    particle_sum.append(val)

dp=[[0]*(N+1) for _ in range(4)]

for i in range(1,4):    
    for j in range(i*T,N+1):
        dp[i][j]=max(dp[i][j-1],dp[i-1][j-T]+particle_sum[j]-particle_sum[j-T]) #객차를 현재 객차로 변경하는 경우와, 변경하지 않고 비교하는 경우 중 큰 값을 선택

print(dp[3][N]) #3대를 운행 했을 때의 가장 마지막 객차와의 비교를 마친 dp[3][N]의 값을 출력

