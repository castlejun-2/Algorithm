import sys
from collections import defaultdict
input=sys.stdin.readline

N,M,B=map(int,input().split())
block=defaultdict(int)
total=0;length=N*M

for _ in range(N):
    for i in map(int,input().split()):
        block[i]+=1
        total+=i
        
min_val=sorted(block.keys())[0]
max_val=sorted(block.keys())[-1]

answer=[float('inf'),-1]

for t in range(min_val,max_val+1):  #최소값부터, 최대값까지만 탐색
    if length*t <= total+B:         #만들고자 하는 블록의 높이가 갖고있는거보다 적어야 한다.
        sec=0
        for key in block.keys():
            if key<t:               #만들고자 하는 높이보다 작다면 블록을 쌓아야 하므로 1초의 시간 소요
                sec+=(t-key)*(block[key])
            else:                   #만들고자 하는 높이보다 높다면 블록을 깎아야 하므로 2초의 시간 소요
                sec+=(key-t)*(block[key])*2
        if answer[0]>=sec:          #더 적게 소요된다면, answer값 갱신 (이때, 높이가 큰 것이 우선순위이므로 같다 부등호 추가)
            answer=[sec,t]
print(*answer)
