def rotate(que,board):
    x1,y1,x2,y2=que[0],que[1],que[2],que[3]
    tmp=board[x1][y1]
    stack=[tmp]
    #왼쪽 라인 변경
    for i in range(x1,x2):
        board[i][y1]=board[i+1][y1]
        stack.append(board[i][y1])
    #아래쪽 라인 변경
    for i in range(y1,y2):
        board[x2][i]=board[x2][i+1]
        stack.append(board[x2][i])
    #오른쪽 라인 변경
    for i in range(x2,x1,-1):
        board[i][y2]=board[i-1][y2]
        stack.append(board[i][y2])
    #위측 라인 변경
    for i in range(y2,y1,-1):
        board[x1][i]=board[x1][i-1]
        stack.append(board[x1][i])
    board[x1][y1+1]=tmp
    return min(stack),board #변환된 board와, 테두리 값중 가장 작은 값 반환
    
def solution(rows, columns, queries):
    board=[[j+1+(columns*i) for j in range(columns)] for i in range(rows)]
    answer = []
    for que in queries:
        ans,board=rotate(list(map(lambda x:x-1,que)),board)
        answer.append(ans)  #해당 회차 rotate에서 가장 작았던 값을 answer에 push
    return answer