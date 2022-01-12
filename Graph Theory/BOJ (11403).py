from sys import stdin

N=int(stdin.readline().strip())
g_list=[list(map(int,stdin.readline().split())) for _ in range(N)]

def dfs(i):
    global visited
    for k in range(N):                  #시작 정점에서 도착정점을 방문하지 않았는데, 연결되어 있다면 방문여부를 체크하고 해당 지점에서 이어져 있는 경로까지 dfs로 탐색
        if visited[k]==0 and g_list[i][k]==1:
            visited[k]=1
            dfs(k)

for i in range(N):                      #각 정점별로 방문 할 수 있는 정점을 확인
    visited=[0]*N   
    dfs(i)
    print(" ".join(map(str,visited)))   #각 정점별로 방문 할 수 있는 정점을 출력
