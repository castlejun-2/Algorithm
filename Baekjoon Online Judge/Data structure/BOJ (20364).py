from sys import stdin #input의 갯수가 최대 200,000이므로 입력속도를 향상시켜준다.

N,Q=map(int,input().split())
duck_list=[int(stdin.readline()) for _ in range(Q)]
visited=[0]*N

for k in duck_list:
    tmp=k
    state=0
    while tmp>1:  #최상단 부모노드까지 탐색하여준다.
        if visited[tmp-1]:  #해당 노드에 방문되어 있다면 위치 갱신
            state=tmp
        tmp=tmp//2  #몫을 2로 나누어주면 부모 노드이다.
    print(state)  #방문된 값으로 갱신되었다면 갱신값, 그렇지 않다면 초기값 0이 출력된다.
    visited[k-1]=1
