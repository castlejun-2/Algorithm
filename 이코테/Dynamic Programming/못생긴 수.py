n=int(input())
dp=[0]*n

dp[0]=1
two=2;three=3;five=5
twoIdx=0;threeIdx=0;fiveIdx=0

for i in range(1,n):
    dp[i]=min(two,three,five)   #2,3,5를 곱하면서 배열을 형성하는 것을 알 수 있다.
    if dp[i]==two:
        twoIdx+=1
        two=2*dp[twoIdx]
    if dp[i]==three:
        threeIdx+=1
        three=3*dp[threeIdx]
    if dp[i]==five:
        fiveIdx+=1
        five=5*dp[fiveIdx]
        
print(dp[n-1])
