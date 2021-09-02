import sys
input=sys.stdin.readline

N=int(input())
for i in range(N):
    dp=[1,1,1,2,2]
    K=int(input())
    if(K<6):                          #6번째 index부터 수열이 성립한다.
        print(dp[K-1])      
        continue
    for j in range(5,K):
        dp.append(dp[j-1]+dp[j-5])    #dp[k]=dp[k-1]+dp[k-5] 이고 다음과 같이 append를 통해 리스트에 추가하여준다.
    print(dp[K-1])                    #K번째 수는 K-1의 index 위치의 수이므로 다음과 괕이 출력하여준다.
