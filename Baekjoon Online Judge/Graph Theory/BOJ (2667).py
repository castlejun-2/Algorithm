import sys
input=sys.stdin.readline

dx = [-1, 1, 0, 0]                   #좌,우 비교를 위한 배열
dy = [0, 0, 1, -1]                   #상,하 비교를 위한 배열

def dfs(row,col,apartment):
    visit[row][col]=1
    global cnt
    dfslist[row][col]=apartment      #해당 단지의 아파트단지로 값 변경
    cnt+=1
    for i in range(4):
        x=row+dx[i]
        y=col+dy[i]
        if 0 <= x < N and 0 <= y < N:
            if(dfslist[x][y]==1 and visit[x][y]==0):
                dfs(x,y,apartment)    
    
if __name__ == "__main__":
    N=int(input())                       #N X N matrix 생성을 위한 N값 입력
    dfslist = [[0]*N for _ in range(N)]  #아파트 단지의 위치 list
    visit = [[0]*N for _ in range(N)]    #방문 list 
    dfslist=[list(map(int, input().strip())) for _ in range(N)]
    cntlist=[]                           #각 아파트단지의 아파트 갯수를 담기 위한 배열
    cnt=0;                               #각 아파트단지별 아파트 갯수
    apartment=0;
    
    for a in range(N):
        for b in range(N):
            if dfslist[a][b]==1 and visit[a][b]==0:
                dfs(a,b,apartment+1)
                cntlist.append(cnt)
                cnt=0                    #아파트단지별 아파트 갯수 초기화
                apartment+=1             #아파트단지 이름 변경
                
print(apartment)                         #아파트단지의 이름 만큼 지어진 것이므로 len(cntlist)와 같은 의미이기에 len을 통한 함수계산보다 빠르게 계산될 수 있도록 apartment 변수를 활용하여준다. 
for k in sorted(cntlist):                #sorted 함수를 통해 정렬된 객체를 반환하여 k에 넣어준 후 출력하여준다.
    print(k)
