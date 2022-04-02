from collections import deque 

dx=[0,0,1,-1]
dy=[1,-1,0,0]

if __name__=="__main__":
    a,b=map(int,input().split())
    m_list=[list(map(int,input().split())) for _ in range(b)]

    dq=deque([])

    for i in range(a):
        for j in range(b):
            if m_list[j][i]==1:                 #초기에 익은 토마토의 위치를 deque에 저장
                dq.append([j,i])

    while dq:
        y,x=dq.popleft()
        for i in range(4):                      #상하좌우를 확인하기 위해 반복
            nx=x+dx[i]                        
            ny=y+dy[i]
            if 0<=nx<a and 0<=ny<b and m_list[ny][nx]==0:
                dq.append([ny,nx])              #이제 익은 토마토가 되었으므로 deque에 인덱스 추가
                m_list[ny][nx]=m_list[y][x]+1   #m_list가 0이라면 옆에 있는 익은 토마토에 영향을 받은것이므로 이전 m_list까지 걸린 날짜에 +1을 담은 정보를 저장
    
    day=0
    for i in range(a):
        for j in range(b):
            if m_list[j][i]!=0:               #m_list가 0이 아니라면 최대 일수를 비교해서 큰 일수를 저장
                day=max(day,m_list[j][i])
            else:
                day=-2                        #m_list가 0이라면 day를 -2로 바꾸어주고 반복문 탈출
                break
        if day==-2:                           #day==-2로 flag로 활용하여 다시한번 반복문 탈출
            break
        
    if day!=-2:
        print(day-1)                          #flag가 활성화 되어있지 않다면 최대 일자에서 -1 해주어 출력
    else:
        print(-1)                             #flag가 활성화 되어 있다면 -1 출력
