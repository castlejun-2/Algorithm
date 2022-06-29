from sys import stdin

N,M=map(int,input().split())
square=[list(map(int,stdin.readline().split())) for _ in range(N)]

dx=[-1,0,0,1]
dy=[0,-1,1,0]

def dfs(x,y,tsum,cnt):  #회전, 대칭을 하여 생성되는 모든 도형의 모형은 현재 방향을 기점으로 거리가 4인 경로들이다.
    global answer
    if answer>=tsum+max_val*(4-cnt):    #이후에 생성 가능한 최대값이 answer보다 작을경우 더 탐색할 필요가 없다.
        return
    if cnt==4:
        answer=max(answer,tsum)
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            if cnt==2:  #ㅗ,ㅓ,ㅜ,ㅏ 모형인 경우, 현재위치까지 탐색 후 이전 위치로 돌아가 재 탐색한다
                visited[nx][ny]=1
                dfs(x,y,tsum+square[nx][ny],cnt+1)
                visited[nx][ny]=0
            visited[nx][ny]=1   #그외의 도형의 경우 현재 위치로부터 더 뻗어나간다.
            dfs(nx,ny,tsum+square[nx][ny],cnt+1)
            visited[nx][ny]=0

answer=0
max_val=max(map(max,square))    #생성 가능한 최댓값을 활용하기 위해 2차원 배열의 최댓값을 구한다.
visited=[[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j]=1
        dfs(i,j,square[i][j],1)
        visited[i][j]=0

print(answer)