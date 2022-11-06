def solution(n, results):
    answer = 0
    graph = [[0]*n for _ in range(n)]
    
    for result in results:
        graph[result[0]-1][result[1]-1]=1
        graph[result[1]-1][result[0]-1]=-1
    for i in range(n):
        for j in range(n):
            for k in range(n):      #1이 2를 이기고, 2가 3을 이기면 1은 3을 이긴것이다.
                if graph[i][j]==1 and graph[j][k]==1:
                    graph[i][k]=1
                    graph[k][i]=-1
                if graph[i][j]==-1 and graph[j][k]==-1:
                    graph[i][k]=-1
                    graph[k][i]=1
    for i in range(n):              #자신의 순위를 알기 위해서는 n-1명과의 결과를 알아야 한다.
        if graph[i].count(1)+graph[i].count(-1)==n-1:
            answer+=1
    return answer   
