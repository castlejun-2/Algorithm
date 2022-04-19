from sys import stdin
from collections import deque

N,M=map(int,stdin.readline().strip().split())
ice_box=[list(map(int,stdin.readline().strip())) for _ in range(N)]

visited=[[0]*M for _ in range(N)]
dq=deque()
cnt=0

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and not ice_box[nx][ny]:
            visited[nx][ny]=1
            dfs(nx,ny)
        

for i in range(N):
    for j in range(M):
        if not visited[i][j] and not ice_box[i][j]:
            visited[i][j]=1
            dfs(i,j)
            cnt+=1
print(cnt)
