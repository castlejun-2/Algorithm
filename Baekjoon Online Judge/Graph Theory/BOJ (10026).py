from sys import stdin
import sys

sys.setrecursionlimit(10000)  #재귀 함수의 깊이 설정

dx=[0,0,1,-1]
dy=[-1,1,0,0]

def get_normal(x,y,color):  #일반 구역 구하는 함수
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and color_list[nx][ny]==color:
            get_normal(nx,ny,color)

def get_color_weakness(x,y,color):  #적록색약 구역 구하는 함수
    weakness_visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and weakness_visited[nx][ny]==0 and color_weakness_list[nx][ny]==color:
            get_color_weakness(nx,ny,color)

N=int(stdin.readline())
color_list=[list(map(str,stdin.readline().strip())) for _ in range(N)]
color_weakness_list=[]
for cl in color_list: #Red와 Green을 같은 함수로 보기 때문에, R을 G로 치환해 새로운 리스트를 저장하여 준다.
    temp_list=[]
    for c in cl:
        temp=c.replace('R','G')
        temp_list.append(temp)
    color_weakness_list.append(temp_list)

visited=[[0]*N for _ in range(N)] #해당 영역의 방문을 확인하여준다.
weakness_visited=[[0]*N for _ in range(N)]
normal_cnt=0
weakness_cnt=0

for i in range(N):  #방문하지 않은 곳들을 시작점으로 구역을 설정한다.
    for j in range(N):
        if visited[i][j] == 0:
            get_normal(i,j,color_list[i][j])
            normal_cnt+=1
for i in range(N):
    for j in range(N):
        if weakness_visited[i][j] == 0:
            get_color_weakness(i,j,color_weakness_list[i][j])
            weakness_cnt+=1
print(normal_cnt,weakness_cnt)
