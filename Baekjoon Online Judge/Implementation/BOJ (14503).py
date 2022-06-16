dx=[-1,0,1,0]
dy=[0,1,0,-1]

N,M=map(int,input().split())
r,c,d=map(int,input().split())
location_list=[list(map(int,input().split())) for _ in range(N)]
answer=1

location_list[r][c]=2 #처음 위치 방문처리

while True:
    flag=0
    
    for _ in range(4):
        d=(d-1)%4 #현재 방향을 기준으로 왼쪽 회전
        
        nx=r+dx[d]
        ny=c+dy[d]
        
        if 0<=nx<N and 0<=ny<M and location_list[nx][ny]==0:  #왼쪽 위치가 비어있다면 청소하고 해당 위치로 이동
            location_list[nx][ny]=2
            answer+=1
            r=nx
            c=ny
            flag=1
            break
            
    if flag==0: #4방향 모두 진입하는데 실패하였다면 후진하는 칸이 빈 곳인지 확인
        nx=r+dx[(d-2)%4]
        ny=c+dy[(d-2)%4]
        if 0<=nx<N and 0<=ny<M and location_list[nx][ny]==1:
            print(answer)
            break
        else: #비어있지 않다면 현재 방향을 기준으로 후진
            r=r+dx[(d-2)%4] #현재 방향 d에서 -2로 해준 후 나눠주면 반대방향으로 전진하는 효과를 얻음
            c=c+dy[(d-2)%4]
