def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]:
                if bucket and bucket[-1]==board[i][move-1]: #위에 같은 값이 쌓이면 2개의 인형이 사라지게 된다.
                    bucket.pop()
                    answer+=2
                else: #바구니의 가장 위에 있는 인형이 해당 인형과 같지 않다면 바구니에 인형을 추가해준다.
                    bucket.append(board[i][move-1])
                board[i][move-1]=0  #인형은 크레인이 뽑아갔으므로 해당 자리는 0이 된다.
                break 
    return answer
