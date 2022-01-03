from sys import stdin
import sys

sys.setrecursionlimit(10000)          #재귀의 최대 깊이를 설정하여준다.

N = int(stdin.readline().strip())

dx = [0,-1,1,0]
dy = [1,0,0,-1]
r_list = [list(map(int,stdin.readline().split())) for _ in range(N)]
r_min = min(map(min,r_list))          #리스트 내에서 가장 작은 빌딩의 높이를 찾는다.
r_max = max(map(max,r_list))          #리스트 내에서 가장 높은 빌딩의 높이를 찾는다.
cnt = 1                               #비가 아예 오지 않을수도 있으므로 최소값을 1로 설정하여준다.

def dfs(x,y):
    global rain
    visited[x][y]=1
    for i in range(4):    #상하좌우 인접한 영역을 확인하여준다.
        a=x+dx[i]
        b=y+dy[i]
        if 0<=a<N and 0<=b<N and r_list[a][b]>rain and not visited[a][b]:  #인접한 영역이 지금 비의 높이보다 높고 방문하지 않았다면 방문하여준다.
            dfs(a,b)

for rain in range(r_min,r_max):             #비의 높이를 빌딩의 가장 낮은 높이부터 가장 높은높이-1까지 비교한다. 비의 높이를 가장 높은 빌딩의 높이로 설정하면 안전지대가 어짜피 0이다.
    visited = [[0]*N for _ in range(N)]     #방문 횟수를 비의 높이마다 초기화해준다.
    t_cnt = 0                               #가장 많은 안전지대를 적용시킬 변수를 설정해준다.
    for i in range(N):
        for j in range(N):
            if r_list[i][j]>rain and visited[i][j]==0:  #해당 영역이 지금 비의 높이보다 높고 방문하지 않았다면 방문하여준다.
                dfs(i,j)
                t_cnt+=1
    cnt=max(cnt,t_cnt)            
print(cnt)
