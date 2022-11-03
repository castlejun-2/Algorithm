import sys
sys.setrecursionlimit(10**9)

def solution(grid):
    def dfs(grid,x,y,d,cnt):
        nx=x; ny=y; nd=d;
        if grid[x][y]=='L':
            nx=(x+dx[(d-1)%4])%len(grid)
            ny=(y+dy[(d-1)%4])%len(grid[0])
            nd=(d-1)%4
        elif grid[x][y]=='R':
            nx=(x+dx[(d+1)%4])%len(grid)
            ny=(y+dy[(d+1)%4])%len(grid[0])
            nd=(d+1)%4
        elif grid[x][y]=='S':
            nx=(x+dx[d])%len(grid)
            ny=(y+dy[d])%len(grid[0])
        if graph[x][y][nd]:           #현재 방향에서 주어진 방향으로 뻗어나간 적이 있는 경우 = 사이클 존재
            answer.append(cnt)        #cnt를 값에 추가
            return
        graph[x][y][nd]=1
        dfs(grid,nx,ny,nd,cnt+1)      #사이클이 아직 형성되지 않은 경우 
        
    answer = []    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    graph = [[[0]*4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4): 
                if not graph[i][j][k]:  #현재 방향으로 아직 탐색하지 않은 경우
                    graph[i][j][k]=1
                    dfs(grid,(i+dx[k])%len(grid),(j+dy[k])%len(grid[0]),k,1)
    
    return sorted(answer)
