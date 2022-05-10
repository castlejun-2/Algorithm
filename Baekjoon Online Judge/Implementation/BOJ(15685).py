from sys import stdin

move=[(1,0),(0,-1),(-1,0),(0,1)]
square=[(0,1),(1,0),(1,1)]

N=int(stdin.readline().strip())
dragon_list=[list(map(int,stdin.readline().strip().split())) for _ in range(N)]
visited_list=[[0]*101 for _ in range(101)]
answer=0

for x,y,d,g in dragon_list:
    curve=[d]
    visited_list[x][y]=1
    for _ in range(g):  #커브의 규칙을 보면, 이 전 세대의 방향(마지막 선을 기준으로)에 +1이 새로 그려지는 커브의 시작점 방향이 되는 것을 확인 할 수 있다.
        for i in range(len(curve)-1,-1,-1):
            curve.append((curve[i]+1)%4)
    
    for i in range(len(curve)): #해당 좌표를 기준으로 방향을 통해 그려나간다.
        x+=move[curve[i]][0]
        y+=move[curve[i]][1] 
        if 0<=x<=100 and 0<=y<=100:
            visited_list[x][y]=1

for i in range(100):    #정사각형의 갯수를 새어준다.
    for j in range(100):
        if visited_list[i][j]:
            temp_cnt=1
            for k in range(3):
                nx=i+square[k][0]
                ny=j+square[k][1]
                if 0<=nx<=100 and 0<=ny<=100 and visited_list[nx][ny]:
                    temp_cnt+=1
                else:
                    break
            if temp_cnt==4:
                answer+=1
print(answer)