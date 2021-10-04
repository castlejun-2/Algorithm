N=int(input())
square=[i*i for i in range(1,317)]      #N<=100,000 이므로 최대 제곱근인 317까지 square에 미리 저장해둔다.
dp=[0]                                  #Dynamic Programming 기법을 적용한 값들을 넣을 배열 선언
for i in range(1,N+1):
    t_list=[]                           #어느 제곱근으로 왔을 때 가장 효율적인지를 판별해주기 위한 배열 선언
    for j in square:                    #i보다 작은 제곱근들을 꺼내 (i-제곱근(j))+제곱근(j) 를 했을 때 dp값을 비교하여 가장 작은지를 판별한다.
        if j>i:                         #제곱근(j)가 i보다 커지면 중단한다
            break
        t_list.append(dp[i-j])
    dp.append(min(t_list)+1)            #들어있는 dp[i-j]값 중 가장 작은 것을 선택하여 +1(해당 dp값에서 제곱근 만큼 더해주는 것이므로) 해준다.
print(dp[N])                            #최종 결과 출력
