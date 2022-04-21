from sys import stdin
from collections import deque

N,M=map(int,stdin.readline().strip().split())
miro_list=[list(map(int,stdin.readline().strip())) for _ in range(N)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):   #가장 가까운 거리부터 삽입 해나아가면서 값을 바꿔나간다.
    dq=deque()
    dq.append((x,y))
    while dq:
        i,j=dq.popleft()
        for k in range(4):
           nx=i+dx[k]
           ny=j+dy[k]
           if 0<=nx<N and 0<=ny<M and miro_list[nx][ny]==1: #처음 도착 했을 때만 queue에 삽입한다.
               dq.append((nx,ny))
               miro_list[nx][ny]=miro_list[i][j]+1
    return miro_list[N-1][M-1]
print(bfs(0,0))