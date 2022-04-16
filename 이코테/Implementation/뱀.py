from sys import stdin
from collections import deque

dx=[0,1,-1,0]
dy=[1,0,0,-1]

N=int(stdin.readline().strip())
K=int(stdin.readline().strip())
board=[[1]*N for _ in range(N)]
tail=deque([[0,0]])
time=1
dt=0
direction={}
x,y=0,0
board[0][0]=0

for i in range(K):
    a,b=map(int,stdin.readline().strip().split())
    board[a-1][b-1]=2

L=int(stdin.readline().strip())

for i in range(L):
    a,b=map(str,stdin.readline().strip().split())
    direction[int(a)]=b

while True:
    x=x+dx[dt]
    y=y+dy[dt]
    if 0<=x<N and 0<=y<N and board[x][y]:
        if not board[x][y]==2:  #사과가 아니라면
            tx,ty=tail.popleft()
            board[tx][ty]=1 #꼬리 제거
        board[x][y]=0   #머리 삽입
        tail.append([x,y])
        if time in direction.keys():
            if direction[time]=="L":
                dt=(dt-1)%4
            else:
                dt=(dt+1)%4
        time+=1    
    else:
        print(time)
        break