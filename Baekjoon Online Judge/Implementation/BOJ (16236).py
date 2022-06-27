from collections import deque

def bfs(x,y,size):
    q=deque([[x,y]])
    distance=[[0]*N for _ in range(N)]
    visited=[[0]*N for _ in range(N)]
    visited[x][y]=1
    temp=[]
    
    while q:
        x,y=q.popleft() #현재 물고기의 위치를 기준으로 상하좌우를 탐색한다.
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and fish_list[nx][ny]<=size:
                q.append([nx,ny])
                distance[nx][ny]=distance[x][y]+1
                visited[nx][ny]=1
                if fish_list[nx][ny]<size and fish_list[nx][ny]!=0: #먹을 수 있는 물고기라면 먹어준다.
                    temp.append([nx,ny,distance[nx][ny]])   #먹을 수 있는 물고기를 전부 탐색 후 거리순으로 return 하여준다.
    return sorted(temp,key=lambda x:(-x[2],-x[0],-x[1])) #retrun 받은 list는 stack 형태이므로 내림차순으로 정렬해준다.

N=int(input())
fish_list=[list(map(int,input().split())) for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

shark_size=2
answer=0
shark_x,shark_y=0,0
cnt=0

for i in range(N):
    for j in range(N):
        if fish_list[i][j]==9:
            shark_x,shark_y=i,j

while True:
    shark=bfs(shark_x,shark_y,shark_size)   #거리가 가장 짧은, 가장 위쪽인, 가장 왼쪽 기준에서 먹은 물고기의 위치를 받는다.
    
    if len(shark)==0:
        break
    
    fish_list[shark_x][shark_y]=0   #현재 상어의 위치를 빈칸으로 만들어준다.
    shark_x,shark_y,dist=shark.pop()    
    fish_list[shark_x][shark_y]=0   #상어가 이동 한 후의 위치를 빈칸으로 만들어준다.
    answer+=dist    #물고기를 먹기위해 이동한 거리가 시간이므로 시간을 더해준다.
    cnt+=1  #물고기를 한마리 먹었으므로 더해준다.
    
    if cnt==shark_size: #상어의 크기만큼의 물고기를 먹었다면 몸집을 키워준다.
        shark_size+=1
        cnt=0
print(answer)