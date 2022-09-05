def solution(alp, cop, problems):
    problems = sorted(problems,key=lambda x:(x[0],x[1]))
    max_alp=max(list(zip(*problems))[0])
    max_cop=max(list(zip(*problems))[1])
    dp=[[10**9]*(max_cop+1) for _ in range(max_alp+1)]  #가능한 최대 시간은 10**9값으로 설정
    
    alp=min(alp,max_alp)  #최대 알고력이 현재 알고력보다 낮은 경우를 대비
    cop=min(cop,max_cop)  #최대 코딩력이 현재 코딩력보다 낮은 경우를 대비
    
    dp[alp][cop]=0  #기존 지식으로 풀 수 있는 문제는 0의 시간이 든다.
    
    for i in range(alp,max_alp+1):
        for j in range(cop,max_cop+1):
            if i+1<=max_alp:                           #dp의 범위를 초과 할 수도 있으므로
                dp[i+1][j]=min(dp[i+1][j],dp[i][j]+1)  #1초 경과 시 해당 알고력과 코딩력으로 얻을 수 있는 값 저장
            if j+1<=max_cop:
                dp[i][j+1]=min(dp[i][j+1],dp[i][j]+1)
                
            for algo,code,al_rwd,cd_rwd,cost in problems: #각 문제를 풀 때 얻을 수 있는 알고력
                if i>=algo and j>=code:
                    next_alp=min(max_alp,i+al_rwd)        #dp의 범위를 초과 할 수도 있으므로
                    next_cop=min(max_cop,j+cd_rwd)
                    dp[next_alp][next_cop]=min(dp[next_alp][next_cop],dp[i][j]+cost)  #문제를 풀 때 얻는 알고력과 코딩력에 도달 가능한 시간의 최소값 저장
    return dp[max_alp][max_cop]                           #최대 알고력과 최대 코딩력에 도달하는 최소시간 출력
