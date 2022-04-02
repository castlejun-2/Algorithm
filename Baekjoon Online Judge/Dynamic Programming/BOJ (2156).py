if __name__=="__main__":
    N=int(input())
    list=[0]                        #list 배열 선언
    dp=[0]                          #동적프로그래밍 배열 선언
    for i in range(N):              
        K=int(input())        
        list.append(K)              
    dp.append(list[1])              
    if N>1:
        dp.append(list[1]+list[2])  #N은 1일 때 list[2]의 값은 존재하지 않으므로 if문을 통해 조건 설정
    for i in range(3,N+1):          #2번째 인덱스까지 값이 들어가 있으므로 3부터 N까지 돌아갈 수 있도록 반복
        dp.append(max(dp[i-1],list[i]+list[i-1]+dp[i-3],list[i]+dp[i-2]))
    print(dp[N])                    #초기 배열 선언 시 0의 초깃값을 넣어줬으므로 그대로 N번째 index 출력
