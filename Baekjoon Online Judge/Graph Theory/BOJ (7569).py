from sys import stdin
from collections import deque

dx=[-1,0,1,0,0,0]
dy=[0,1,0,-1,0,0]
dh=[0,0,0,0,1,-1]
            
M,N,H=map(int,stdin.readline().split())
tomato_list=[]
dq=deque([])    #토마토가 위치한 위치정보
day=0

for i in range(H):
    temp=[]
    for j in range(N):
        temp.append(list(map(int,stdin.readline().split())))
        for k in range(M):
            if temp[j][k]==1:
                dq.append([i,j,k])
    tomato_list.append(temp)

while dq:
    h,n,m=dq.popleft()
    
    for i in range(6):
        nh=h+dh[i]
        nx=n+dx[i]
        ny=m+dy[i]
        if 0<=nh<H and 0<=nx<N and 0<=ny<M and tomato_list[nh][nx][ny]==0:
            dq.append([nh,nx,ny])
            tomato_list[nh][nx][ny]=tomato_list[h][n][m]+1  #토마토가 익게 될 날짜 정보로 갱신
            
for i in tomato_list:
    for j in i:
        for k in j:
            if k==0:    #익지 않은 토마토가 존재한다면 -1을 출력하고 프로그램 종료
                print(-1)
                exit(0)
        day=max(day,max(j)) #가장 마지막으로 익게된 토마토의 날짜 정보를 저장
print(day-1)

