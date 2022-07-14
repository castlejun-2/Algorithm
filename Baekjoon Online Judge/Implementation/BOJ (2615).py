move=[[0,1],[1,0],[1,1],[-1,1]]    #3개의 방향만 탐색하면 전체 탐색 가능
answer=0
answer_x,answer_y=0,0
board=[list(map(int,input().split())) for _ in range(19)]

def check(direction,color,x,y,cnt):
    global answer,answer_x,answer_y
    if cnt==5:  #다섯줄이 다 채워졌을 경우
        nx=x+move[direction][0]
        ny=y+move[direction][1]
        if 0<=nx<19 and 0<=ny<19 and board[nx][ny]==color:  #6줄이 되지 않았는지 확인
            return
        else:
            if direction==0:
                answer=color
                answer_x=x; answer_y=y-4;
            elif direction==1:
                answer=color
                answer_x=x-4; answer_y=y;
            elif direction==2:
                answer=color
                answer_x=x-4; answer_y=y-4;
            elif direction==3:
                answer=color
                answer_x=x+4; answer_y=y-4;
        return
      
    nx=x+move[direction][0]
    ny=y+move[direction][1]
    if 0<=nx<19 and 0<=ny<19 and board[nx][ny]==color:  #다음 진행 방향의 바둑의 색이 같다면 함수 진행
        check(direction,color,nx,ny,cnt+1)
    
for i in range(19):
    for j in range(19):
        if board[i][j]:
            for k in range(4):
                #이전 방향에 같은 값 확인을 통해 중복과 6줄이 발생 할 수 있는 경우를 사전에 방지
                if 0<=i-move[k][0]<19 and 0<=j-move[k][1]<19 and board[i-move[k][0]][j-move[k][1]]==board[i][j]:
                    continue
                nx=i+move[k][0]
                ny=j+move[k][1]
                if 0<=nx<19 and 0<=ny<19 and board[nx][ny]==board[i][j]:
                    check(k,board[i][j],nx,ny,2)
print(answer)
if answer:  #무승부가 아니라면 바둑의 위치 출력
    print(answer_x+1,answer_y+1)
