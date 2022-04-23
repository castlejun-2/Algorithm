from sys import stdin
from itertools import combinations
import copy

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def find_safe_area(graph):  #안전지대를 찾는다.
    cnt=0
    for i in range(N):
        for j in range(M):
            if graph[i][j]==0:
                cnt+=1
    return cnt

def go_virus(graph,x,y):    #바이러스를 뿌린다
    graph[x][y]=2
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
            go_virus(graph,nx,ny)
    return graph

N,M=map(int,stdin.readline().strip().split())
graph=[list(map(int,stdin.readline().strip().split())) for _ in range(N)]
virus_list=[]
safe=[]
result=0

for i in range(N):
    for j in range(M):
        if graph[i][j]==2:
            virus_list.append([i,j])
        elif graph[i][j]==0:
            safe.append([i,j])

wall_list=list(combinations(safe,3))    #세울 수 있는 벽들의 조합

for wall in wall_list:  #각 경우의 수를 대입해보며 가장 많이 생성되는 안전지대 갯수 출력
    copy_graph=copy.deepcopy(graph)
    for w in wall:  #벽 setting
        a,b=map(int,w)
        copy_graph[a][b]=1
    for virus in virus_list:    #바이러스의 시작점부터 바이러스 퍼뜨리기
        x,y=map(int,virus)
        go_virus(copy_graph,x,y)
    result=max(result,find_safe_area(copy_graph))   #바이러스를 뿌린 후, 안전지대의 갯수 비교
print(result)