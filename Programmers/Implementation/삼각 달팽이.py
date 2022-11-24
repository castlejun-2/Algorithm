def solution(n):
    answer = [[0]*n for _ in range(n)]
    count = 1
    col = 0; row = -1
    for i in range(n,-1,-3):
        for j in range(i):
            row+=1;     #행과 열의 값을 먼저 반영해주어야 한다.
            answer[row][col]=count
            count+=1;
        for j in range(i-1):
            col+=1;
            answer[row][col]=count
            count+=1;
        for j in range(i-2):
            col-=1; row-=1;
            answer[row][col]=count
            count+=1
    ans = []
    
    for i in range(1,n+1):
        for j in range(1,i+1):
            ans.append(answer[i-1][j-1])
    return ans
