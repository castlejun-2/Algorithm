from collections import deque

direction=[[0,1],[0,-1],[-1,0],[1,0]]

N,M,x,y,K=map(int,(input().split()))
map_list=[list(map(int,input().split())) for _ in range(N)]
command=list(map(int,input().split()))
dice=[[0]*3 for _ in range(4)]

def change(dr):
    if dr==4:   #남쪽이면 주사위의 값을 아래로 민다.
        tmp=dice[0][1]
        for i in range(3):
            dice[i][1]=dice[i+1][1]
        dice[3][1]=tmp
    elif dr==3: #북쪽이면 주사위의 값을 위로 민다.
        tmp=dice[3][1]
        for i in range(3,0,-1):
            dice[i][1]=dice[i-1][1]
        dice[0][1]=tmp
    elif dr==2: #서쪽이면 주사위의 값을 왼쪽으로 민다.
        tmp=dice[1][0]
        dice[1][0]=dice[1][1]
        dice[1][1]=dice[1][2]
        dice[1][2]=dice[3][1]
        dice[3][1]=tmp
    else:   #동쪽이면 주사위의 값을 오른쪽으로 민다.
        tmp=dice[1][2]
        dice[1][2]=dice[1][1]
        dice[1][1]=dice[1][0]
        dice[1][0]=dice[3][1]
        dice[3][1]=tmp

dice[3][1]=map_list[x][y]   #맨 처음 지도의 값을 주사위 밑면에 복사

for cm in command:
    d=direction[(cm-1)%4]
    nx=x+d[0]
    ny=y+d[1]
    if 0<=nx<N and 0<=ny<M: #만약 이동한 칸이 지도의 범위 이내라면 작업 수행
        change(cm)
        if map_list[nx][ny]==0: #만약 지도의 칸이 0이면 주사위 밑면 복사
            map_list[nx][ny]=dice[3][1]
        else:   #그렇지 않으면 지도를 0으로 만들고 지도의 칸의 값을 주사위의 밑면으로 복사
            dice[3][1]=map_list[nx][ny]
            map_list[nx][ny]=0 
        x=nx
        y=ny
        print(dice[1][1])   #주사위의 윗면 출력