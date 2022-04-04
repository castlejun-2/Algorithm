from sys import stdin
from itertools import combinations

N,M=map(int,stdin.readline().strip().split())
ball_list=list(map(int,stdin.readline().split()))

comb_list=list(combinations(ball_list,2))
cnt=0

for i in comb_list:
    a,b=map(int,i)
    if a!=b:
        cnt+=1
print(cnt)