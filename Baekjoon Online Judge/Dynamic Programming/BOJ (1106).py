C,N=map(int,input().split()) #목표치, 홍보할 수 있는 도시
info=[]
dp=[100001]*(C+101) #고객으로 최대 100명까지 더 확보 할 수 있으므로 여유잡아 C+101 만큼의 메모리 확보
dp[0]=0
for _ in range(N):
    cost,benefit=map(int,input().split())   #드는 비용, 유치 가능 인원
    info.append([cost,benefit])

for cost,customer in info:
    for c in range(customer,C+101): #더 많은 인원을 모집하는 비용이 적을 수 있다.
        dp[c]=min(dp[c],dp[c-customer]+cost) #dp[c]=c명을 구하기 위해 드는 최소비용, dp[c-유치가능인원]+유치 비용 vs dp[c]
print(min(dp[C:C+101])) #C명을 유치하는데 드는 최소비용
