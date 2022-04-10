from sys import stdin

N=int(stdin.readline().strip())
direction=list(map(str,stdin.readline().strip().split()))

x,y=1,1
dx=[0,0,1,-1]
dy=[1,-1,0,0]
move=['R','L','D','U']  #위의 dx,dy에 맞춰 방향 타입 설정

for dir in direction:
    for i in range(4):
        if dir==move[i]:    #방향 타입에 맞춰 x,y변수 이동시 위치 확인
            nx=x+dx[i]
            ny=y+dy[i]
    if 0<nx<=N and 0<ny<=N: #이동 시 유효범위 내에 있으면 값 수정
        x,y=nx,ny
print(x,y)   
