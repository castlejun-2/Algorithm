from sys import stdin

N,K=map(int,stdin.readline().split())
cnt=0

while N>=K:
    share=(N//K)*K
    cnt+=(N-share) #한번에 나누어 질 수 있도록 -1 연산 과정을 한번에 처리
    N=share
    N//=K 
    cnt+=1
if N==1:
    print(cnt)
else:
    print(cnt+K-N)  #N을 더이상 K로 나눌 수 없을 때 -1 연산 과정을 한번에 처리