A=input()
B=input()

A_len=len(A)
B_len=len(B)

dp=[[0]*(B_len+1) for _ in range(A_len+1)]

for i in range(1,A_len+1):
    dp[i][0]=i
for i in range(1,B_len+1):
    dp[0][i]=i
    
for i in range(1,A_len+1):
    for j in range(1,B_len+1):
        if A[i-1]==B[j-1]:  #문자가 같다면 비용이 들지 않으므로, 각 문자가 존재하지 않았던 이 전의 dp값을 그대로 가져온다.
            dp[i][j]=dp[i-1][j-1]
        else:   #문자가 같지 않다면, 삽입, 삭제, 교환 중 가장 저렴한 비용에 +1을 한 값을 삽입한다.
            dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])

print(dp[A_len-1][B_len-1])
