def solution(n):
    answer = [[0]*n for _ in range(n)]
    count = 1
    col = 0; row = 0
    for i in range(n-1,-1,-3):
        for j in range(i):
            answer[row][col]=count
            row+=1; count+=1;
        for j in range(i-1):
            answer[row][col]=count
            col+=1; count+=1;
        for j in range(i-2):
            answer[row][col]=count
            col-=1; row-=1; count+=1
    
    ans = []
    
    for i in range(1,n+1):
        for j in range(i):
            ans.append(answer[i-1][j-1])
    return ans
