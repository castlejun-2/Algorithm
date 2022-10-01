import sys
input=sys.stdin.readline

N=int(input())
town=[]
_sum=[0]

for i in range(N):
    idx,num=map(int,input().split())
    town.append([idx,num])

town.sort()             #위치별로 나와있지 않을 수 있으므로
    
for idx,num in town:    #누적합 계산
    _sum.append(num+_sum[-1])

for i in range(1,N+1):  #인구의 절반에 위치한 index가 최소값을 형성
    if _sum[i]>=_sum[-1]/2:
        print(town[i-1][0])
        break
