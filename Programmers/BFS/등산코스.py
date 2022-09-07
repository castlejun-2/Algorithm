import heapq

def solution(n, paths, gates, summits):
    answer=[0,10**7+1]
    visited=[10**7+1]*n
    summits=set(summits)  #in 연산의 경우 set을 사용하면 O(1) but list를 사용하면 O(N) 시간 소요
    graph={i+1:[] for i in range(n)}
    dq=[]
        
    for i,j,w in paths:
        graph[i].append([j,w])
        graph[j].append([i,w])
            
    for gate in gates:
        heapq.heappush(dq,(0,gate)) #최대 힙에 출발 node 입력
        visited[gate-1]=0           #출발 노드까지의 intensity값은 0으로 설정
        
    while dq:
        num,node=heapq.heappop(dq)
        if node in summits or visited[node-1]<num:  #노드가 도착노드이거나, 해당 노드로 오는 간선의 길이가 현재 노드가 갖는 intensity보다 큰 경우 다음 반복 실행
            continue
            
        for number,weight in graph[node]:
            tmp_intensity=max(weight,num)           #출발노드까지 오는 최대 intensity값과 현재 간선의 weight 비교
            if tmp_intensity < visited[number-1]:   #다음 도착 node가 갖게 될 최대 intensity보다 더 빨리 도착 노드에 도착하는 경우 제외 
                visited[number-1]=tmp_intensity
                heapq.heappush(dq,(tmp_intensity,number))
    
    for summit in sorted(summits):
        if visited[summit-1] < answer[1]:
            answer[1]=visited[summit-1]
            answer[0]=summit
    return answer
