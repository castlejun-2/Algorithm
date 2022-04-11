from sys import stdin

N,M=map(int,stdin.readline().strip().split())
A,B,D=map(int,stdin.readline().strip().split())
map_list=[list(map(int,stdin.readline().strip().split())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
visited[A][B]=1
cnt=1
turn_cnt=0

def turn_left():
    global D
    D=(D-1)%4

while True:
    turn_left()
    nx=A+dx[D]
    ny=B+dy[D]
    if visited[nx][ny]==0 and map_list[nx][ny]==0:  #아직 방문하지 않았고, 바다가 아닌경우
        visited[nx][ny]=1
        A=nx
        B=ny
        cnt+=1
        turn_cnt=0
        continue
    else:   #가본곳이거나, 바다인 경우 방향을 회전한다.
        turn_cnt+=1 
    if turn_cnt==4: #이 때 방향 회전을 이미 다 해본 상태라면 뒤로 이동
        nx=A-dx[D]
        ny=B-dy[D]
        if map_list[nx][ny]==1: #뒤가 바다이기 때문에 이동이 불가능하다면 반복문 탈출
            break    
        else:   #뒤가 육지라면 뒤로 이동
            A=nx
            B=ny
            turn_cnt=0  #회전 횟수 초기화
print(cnt)