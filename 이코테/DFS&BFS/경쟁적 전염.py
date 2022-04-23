from sys import stdin
import heapq

dx=[0,0,-1,1]
dy=[1,-1,0,0]

N,K=map(int,stdin.readline().strip().split())
test_tube_list=[list(map(int,stdin.readline().strip().split())) for _ in range(N)]
S,X,Y=map(int,stdin.readline().strip().split())
virus_list=[]
time=0

for i in range(N):
    for j in range(N):
        if test_tube_list[i][j]>0:
            heapq.heappush(virus_list,[test_tube_list[i][j],i,j])

while time!=S and virus_list:   #시간이 종료되거나, 더이상 전염될 곳이 없으면 종료
    time+=1
    temp_virus=[]
    while virus_list:   #현재 존재하는 바이러스의 위치들을 받아온다
        temp_virus.append(heapq.heappop(virus_list)) #바이러스들은 heapq로 정렬되어 들어가므로 앞에서부터 숫자가 작은 숫자부터 정렬되어 있다.
    for virus in temp_virus:    
        val,x,y=virus
        for i in range(4):  #각 바이러스들을 상하좌우로 전염시킴
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and not test_tube_list[nx][ny]:  #0의 값을 갖는 곳만 전염시킨다
                test_tube_list[nx][ny]=val
                heapq.heappush(virus_list,[val,nx,ny])  #새로 전염된 곳들을 virus list에 삽입한다.
print(test_tube_list[X-1][Y-1])