from sys import stdin

str_A = list(map(str,stdin.readline().strip()))     #'A','B','C' 로 각 문자열을 list에 저장
str_B = list(map(str,stdin.readline().strip()))

dp = [[0]*(len(str_B)+1) for _ in range(len(str_A)+1)]  #'A'와 아무것도 없는 문자를 비교해야 할수도 있으므로 string의 길이보다 +1만큼 큰 공간의 배열 할당

for i in range(1,len(str_A)+1):                         #0부터 문자열 str_A의 길이까지 반복
    for j in range(1,len(str_B)+1):                     #0부터 문자열 str_B의 길이까지 반복
        if str_A[i-1]==str_B[j-1]:                      #끝의 문자가 같으면 ex)'ABC'와 'AC' 즉 끝의 C가 같다면 'AB'와 'A' 즉 dp[2][1]의 값에서 +1 해준다.
            dp[i][j]=dp[i-1][j-1]+1
        else:                                           #끝의 문자가 같지 않다면 ex)'ABC'와 'AB' 즉 끝의 C와 B가 다르므로 'AB' 'AB'의 값 dp[2][2]과 'ABC' 'A'의 값 dp[3][1]
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])         #에서 더 큰 값 dp[2][2] = 2, dp[3][1] = 1의 값 max(dp[2][2],dp[3][1]) = 2을 넣어준다.
            
print(dp[len(str_A)][len(str_B)])
