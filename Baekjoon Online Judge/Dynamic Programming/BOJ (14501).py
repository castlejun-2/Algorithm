if __name__=="__main__":
    N=int(input())
    t=[]                               #일을 하는데 걸리는 시간
    w=[]                               #일을 완료하였을 때의 값(무게)
    dp=[]                              #각 요일별 최고 이득
    for i in range(N):
        a,b=map(int,input().split())   #map함수를 통해 t,p 쌍을 N번만큼 반복하여 받는다.
        t.append(a)
        w.append(b)
        dp.append(w)
    dp.append(0)                       #dp[N] 값이 비교를 위해 필요하므로 마지막에 0값을 더해준다.
    for i in range(N-1,-1,-1):         #dp[N-1]부터 dp[0]까지의 순서로 값을 추적해 나아간다. 
        if i+t[i]>N:                   #걸리는 시간이 가능한 요일보다 초과되면 그 다음날의 최고 이득을 따른다.
            dp[i]=dp[i+1]        
        else:    
            dp[i]=max(dp[i+1],w[i]+dp[i+t[i]]) #다음날의 최고이득과 현재 자신이 일을 했을 때의 값과 i+t[i]날의 값을 더한값을 비교해 dp[i]에 넣는다.
    print(dp[0])                       #최종적으로 dp[0] 즉, 시작날의 최대 이득을 출력한다.
