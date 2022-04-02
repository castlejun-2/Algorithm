import sys
sys.setrecursionlimit(10**6)    #재귀함수 최대 깊이 조정

dm=[0, 0, 1, -1]
dn=[1,-1, 0, 0]

def bfs(y,x):                   #넓이 우선 탐색 함수
    g_list[y][x]=0              #이동한 배추는 탐색이 완료되었으므로 1->0으로 수정
    for i in range(4):          #상하좌우를 살펴 배추가 존재한다면 해당 index로 이동
        a=y+dn[i]
        b=x+dm[i]
        if 0<=a<N and 0<=b<M and g_list[a][b]==1:
            bfs(a,b)            #배추가 존재하는 해당 index의 상하좌우를 살피기 위해 bfs() 호출
                
T=int(input())                  #Test 갯수
for _ in range(T):    
    M,N,K=map(int,input().split())
    g_list=[[0]*M for _ in range(N)]
    cnt=0                       #필요한 지렁이의 갯수
    for i in range(K):
        a,b=map(int,input().split())
        g_list[b][a]=1          #배추가 존재하는 위치를 0->1로 수정
    for i in range(N):          #범위 내의 모든 index를 탐색
        for j in range(M):      
            if g_list[i][j]==1:
                bfs(i,j)        
                cnt+=1          #위의 bfs를 거치면 연결되어 있는 배추무리는 전부 1->0으로 변경됨으로 해당 작업을 마친후 cnt +1 증가
    print(cnt)                  #최종 지렁이의 갯수 출력
