import sys
import copy
input=sys.stdin.readline

N=int(input().strip())
now=list(map(int,input().strip()))
final=list(map(int,input().strip()))
answer=0
ans=100001

tmp_final=copy.deepcopy(final)

for i in range(1,N-1):              #첫번째 스위치를 누르지 않은 경우
    if now[i-1]!=tmp_final[i-1]:    #앞의 전구 상태가 같지 않다면 switching
        answer+=1
        for k in range(i-1,i+2):
            tmp_final[k]=1-tmp_final[k]

if now[N-2]!=tmp_final[N-2]:
    answer+=1
    tmp_final[N-2]=1-tmp_final[N-2]
    tmp_final[N-1]=1-tmp_final[N-1]

if tmp_final == now:
    ans=min(ans,answer)
    
final[0]=1-final[0]                 #첫번째 스위치를 누르는 경우
final[1]=1-final[1]

tmp_final=copy.deepcopy(final)
answer=1

for i in range(1,N-1):              
    if now[i-1]!=tmp_final[i-1]:    #앞의 전구 상태가 같지 않다면 switching
        answer+=1
        for k in range(i-1,i+2):
            tmp_final[k]=1-tmp_final[k]

if now[N-2]!=tmp_final[N-2]:
    answer+=1
    tmp_final[N-2]=1-tmp_final[N-2]
    tmp_final[N-1]=1-tmp_final[N-1]

if tmp_final == now:
    ans=min(ans,answer)
    
print(ans if ans!=100001 else -1)