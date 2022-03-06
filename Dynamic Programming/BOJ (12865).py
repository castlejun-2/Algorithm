from sys import stdin

N,K=map(int,stdin.readline().split())
dp_weight=[0]*(K+1)

for i in range(N):
    w,v=map(int,stdin.readline().split())
    for j in range(K,w-1,-1):
        dp_weight[j]=max(dp_weight[j],dp_weight[j-w]+v) #해당 물체의 무게를 포함하지 않았을 때의 value와, 해당 물체의 무게를 포함했을 때의 value 비교 
print(dp_weight[K])
