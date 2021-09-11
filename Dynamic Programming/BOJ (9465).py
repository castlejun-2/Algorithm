if __name__=="__main__":
    N=int(input())
    for _ in range(N):
        K=int(input())
        dp=[list(map(int, input().split())) for _ in range(2)]    #ex) [[50, 10, 100, 20, 40], [30, 50, 70, 10, 60]] 와 같이 배열을 받아준다

        if K==1:                                                  #K==1이면 [0][0] index와 [1][0] 인덱스중 큰 값을 출력해준다  
            print(max(dp[0][0],dp[1][0]))
        else:
            dp[0][1]+=dp[1][0]                                    #(l,t) 라고 한다면, t>1 부터는 t<2 이 전의 값들중 최대값들을 현재 자신의 값들과 더해주어야 하므로
            dp[1][1]+=dp[0][0]                                    #점화식에 넣을 수 없는 t<2 전까지의 값을 넣어준다.
            if K==2:                                              #K==2이면 [0][1] index와 [1][1] 인덱스중 큰 값을 출력해준다      
                print(max(dp[0][1],dp[1][1]))
            else:
                for j in range(2,K):                              #이 전 대각선열의 dp값과, 이 전 대각선열의 왼쪽 dp값 중 큰 값을 선택하여준다.  
                    dp[0][j]+=max(dp[1][j-1],dp[1][j-2])
                    dp[1][j]+=max(dp[0][j-1],dp[0][j-2])
            
                print(max(dp[0][K-1],dp[1][K-1]))                 #마지막 열의 두 값중 큰 값을 선택하여 출력하여준다 
