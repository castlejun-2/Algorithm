dx=[0,1,1]
dy=[1,0,1]

def solution(m, n, board):
    for i in range(m):  #값을 수정할 수 있도록 list로 형변환
        board[i]=list(board[i])
    answer = 0
    
    while True: 
        stack=[]
        for i in range(m):
            for j in range(n):
                if board[i][j]:
                    cnt=0
                    tmp=[(i,j)]
                    for k in range(3):  #오른쪽,아래쪽,아래대각선이 모두 같은 값인지 탐색
                        nx=i+dx[k]
                        ny=j+dy[k]
                        if 0<=nx<m and 0<=ny<n and board[nx][ny]==board[i][j]:
                            cnt+=1
                            tmp.append((nx,ny))
                    if cnt==3:  #같은 값이면 해당 좌표값을 stack에 저장
                        stack+=tmp
        if stack:   #블록이 사라졌으면
            s=list(set(stack))  #중복된 좌표들을 제거하고
            s.sort()            #오름차순으로 좌표를 정렬
            while s:            #해당 좌표값들을 모두 0으로 변경
                x,y=s.pop()
                board[x][y]=0
            for i in range(1,m):    #터진 블록들의 위치에 위의 값들을 삽입
                for j in range(n):
                    if not board[i][j]:
                        for k in range(i,0,-1):
                            board[k][j]=board[k-1][j]
                        board[0][j]=0       
        else:   #만약 이번라운드에 터진 물풍선이 없다면 종료
            break
    for ans in board:   #0으로 터진 블록들의 갯수 계산
        answer+=ans.count(0)
    return answer
