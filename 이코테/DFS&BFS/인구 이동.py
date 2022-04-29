import sys
import copy
sys.setrecursionlimit(10000)

N,L,R=map(int,sys.stdin.readline().strip().split())
country_population=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
move_cnt=0

dx=[0,0,-1,1]
dy=[1,-1,0,0]
answer=0

def dfs(x,y):
    global stack_xy,stack_sum,visited,cnt_sum
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        #L과 R사이이며, 아직 방문하지 않은 곳 탐색
        if 0<=nx<N and 0<=ny<N and L<=abs(country_population[x][y]-country_population[nx][ny])<=R and not visited[nx][ny]:
            visited[nx][ny]=True
            stack_xy.append([nx,ny])    #인덱스를 추가
            stack_sum+=country_population[nx][ny]   #현재 연합의 인구합 추가
            cnt_sum+=1  #현재 연합의 수 추가
            dfs(nx,ny)
while True:
    cnt_sum=1
    stack_xy=[]
    stack_sum=0
    break_state=True
    visited=[[False]*N for _ in range(N)]
    temp_population=copy.deepcopy(country_population)
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:   #아직 방문하지 않았다면
                visited[i][j]=True  #방문 후
                dfs(i,j)    #인근 연합 탐색
                if cnt_sum > 1: #인근 연합의 수가 1보다 크다면
                    stack_xy.append([i,j])
                    stack_sum+=country_population[i][j]
                    while stack_xy: #연합의 위치들의 값들을 수정
                        x,y=stack_xy.pop()
                        temp_population[x][y]=stack_sum//cnt_sum
                    break_state=False
                    stack_sum=0
                    cnt_sum=1   #값 초기화
    country_population=copy.deepcopy(temp_population)   #기존 값들을 변경 시키면, 연합이 적용 된 후의 값으로 읽힐 수 있으므로 copy를 사용
    if break_state: #그 어떠한 연합도 생기지 않았다면 종료
        print(answer)
        break
    answer+=1