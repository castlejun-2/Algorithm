from collections import deque

dx=[-1,0,1,0]       
dy=[0,1,0,-1]

def convert(d,w):           #방향 변환 함수
    if w=="L":              #각 방향이 증가하는 순서에 맞게 dx,dy 설정
        d=(d-1)%4
    else:
        d=(d+1)%4
    return d
    
def snake():
    direction=1                                         #dx,dy의 index로 사용될 값
    time=1                                              #최종 출력 값(게임이 끝나는데에 걸리는 시간)
    x,y=0,0
    snake_tail=deque([[x,y]])                           #꼬리가 위치한 공간을 deque안의 list로 선언
    list[x][y]=2                                        #처음 list[0][0]을 뱀이 위치한 공간으로 선언
    while True:
        x,y=x+dx[direction],y+dy[direction]             #오른쪽으로 1만큼 방향 이동으로 시작 후 변경된 방향인 dx,dy만큼 계속 이동
        if 0<=x<K and 0<=y<K and list[x][y] !=2:        #벽에 부딪히거나 뱀이 자신에게 부딪히지 않았을 때
            if not list[x][y]==1:                       #해당 위치에 사과가 존재하지 않을 때
                t_x,t_y=snake_tail.popleft()            #리스트의 가장 마지막 꼬리 위치를 삭제
                list[t_x][t_y]=0                
            list[x][y]=2                                #도착한 (x,y)의 위치에 뱀 값 입력
            snake_tail.append([x,y])                    #[[x1,y1],[x2,y2]] 와 같이 꼬리 값 입력
            if time in way.keys():                      #현재 시간이 way{} 안에 존재하는지 확인
                direction=convert(direction,way[time])  #존재한다면 현 시간부로 방향을 전환
            time+=1                                     #시간은 반복마다 1초 증가
        else:
            return time                                 #벽에 부딪히거나 뱀이 자신에게 부딪히면 time 값 return
            
if __name__=="__main__":
    K=int(input())                    #K*K 의 2차원 배열 생성을 위한 변수 입력
    A=int(input())                    #Apple의 갯수 입력
    list=[[0]*K for _ in range(K)]    #list[x][y]=0 은 빈 값, list[x][y]=1 은 사과, list[x][y]=2 는 뱀
    for _ in range(A):
        a,b=map(int,input().split())  #Apple의 위치 입력
        list[a-1][b-1]=1              #Apple이 위치해 있는 곳의 값 변경
    S=int(input())                    #방향을 바꾸는 위치 입력
    way={}                            #방향을 바꾸는 시간을 튜플로 생성
    for i in range(S):               
        l,k=input().split()
        way[int(l)]=k                 #만약 17초에 "L"방향으로 바꾼다면 {17: 'L'}을 삽입
    print(snake())
