from collections import deque

#넓이 우선 탐색
def BFS(v):                    
    q=deque()                  #덱을 자료구조로 갖는 변수 선언
    q.append(v)
    visited_b[v]=1             #처음 시작 정점 v의 방문 여부를 1로 선언
    while q:
        v=q.popleft()          #덱이 들어있는 정점을 꺼내 출력
        print(v,end=' ')
        for i in range(1,N+1):                         #1부터 탐색하므로 작은 값 우선으로 탐색 가능
            if visited_b[i]==0 and matrix[v][i]==1:    #이미 방문되어있는 정점은 덱에 추가하지 않음
                q.append(i)                            #방문되어있지 않고, 간선에 의해 연결된 정점을 덱에 삽입
                visited_b[i]=1                         #방문되어있지 않고, 간선에 의해 연결된 정점의 방문 여부 표시
#깊이 우선 탐색
def DFS(v):        
    visited_d[v]=1             #정점의 방문여부를 1로 표시
    print(v,end=' ')
    for i in range(1,N+1):     #1부터 탐색하므로 작은 값 우선으로 탐색 가능
        if matrix[v][i]==1 and visited_d[i]==0:        #간선에 의해 연결되어있고, 아직 정점되지 않은 정점을 갖고
            DFS(i)                                     #해당 정점부터 깊이 우선탐색
    
if __name__=="__main__":
    N,M,V=map(int,input().split())
    out=[]
    matrix=[[0]*(N+1) for _ in range(N+1)]             #1부터 시작하므로 (N+1)*(N+1) 크기의 2차원 배열 선언
    visited_d=[0]*(N+1)
    visited_b=[0]*(N+1)
    for _ in range(M):
        l,k=map(int,input().split())
        matrix[l][k]=1                                 #간선에 의해 연결되는 정점들의 값을 1로 변경
        matrix[k][l]=1
    DFS(V)                                             #깊이 우선 탐색 시작
    print()                                            #한줄 띄어 쓰기
    BFS(V)                                             #넓이 우선 탐색 시작
