from collections import deque

N,M=map(int,input().split())
wall=[list(map(int,input())) for _ in range(N)]
visited=[[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][1]=1
q=deque([[0,0,1]])
answer=N*M

dx=[0,1,0,-1]
dy=[1,0,-1,0]
def bfs():
    while q:
        x,y,v=q.popleft()
        if x==N-1 and y==M-1:   #[N][M] 도달 시 return
            return visited[x][y][v]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if wall[nx][ny]==1 and v==1:  #옆이 벽일 때 뚫을 수 있는 경우
                    visited[nx][ny][0]=visited[x][y][1]+1
                    q.append([nx,ny,0])
                elif wall[nx][ny]==0 and visited[nx][ny][v]==0:  #벽이 아니고 방문하지 않은 경우
                    visited[nx][ny][v]=visited[x][y][v]+1
                    q.append([nx,ny,v])
    return -1   #[N][M]에 도달하지 못하는 경우 -1 리턴

print(bfs())    

