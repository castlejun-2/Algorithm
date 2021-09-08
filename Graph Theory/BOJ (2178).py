if __name__=="__main__":
    N,M=map(int,input().split())                
    dfslist=[]
    index=[[0,0]]                         #index 초기값과 함께 입력
    dx=[-1, 1, 0, 0]      
    dy=[0, 0, 1, -1]
    for i in range(N):
        dfslist.append(list(input()))     #N번만큼 리스트로 만들어서 입력받은 값을 list형(원소는 str형)으로 저장
    dfslist[0][0]=1                       #최단경로의 값을 알기 위해 dfslist[0][0]의 str형을 int형으로 변환
    while index:                          #index가 사라질때까지 반복
        a,b=index[0][0],index[0][1]       #a,b에 (0,0)을 기준으로 시작
        del index[0]                      #index는 a,b에 값을 넣어주고 삭제
        for i in range(4):
            x=a+dx[i]                     #좌우로 탐색
            y=b+dy[i]                     #상하로 탐색
            if 0<=x<N and 0<=y<M and dfslist[x][y]=="1":  #(x,y)에 1이 놓여있는 위치로 탐색 -> 이 때 중복된 값이 발생하지 않는 이유는 아래에서 +1이 있기에 누가 먼저 지나가 있으면 해당 경로는 폐쇄됨으로 오류가 발생하지 않음
                index.append([x,y])                       #(x,y)가 1이면 해당 위치를 푸쉬(상하좌우에 "1"인 위치를 전부 푸쉬)
                dfslist[x][y]=dfslist[a][b]+1             #해당 (x,y)의 위치에 현재까지의 경로의 값에 +1을 더한 값 입력
    print(dfslist[N-1][M-1])                              #최종 dfslist[N-1][M-1]값을 출력하면 최단경로의 위치를 알 수 있음
