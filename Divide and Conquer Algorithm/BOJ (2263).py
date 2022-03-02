from sys import stdin

def preorder(in_start,in_end,post_start,post_end):
    if(in_start>in_end) or (post_start>post_end): return

    #left와 right 구하는 방법 고민

N=int(stdin.readline())
in_list=list(map(int,stdin.readline().split()))
post_list=list(map(int,stdin.readline().split()))
index=[0]*(N+1)

for i in range(N):
    index[in_list[i]]=i

preorder(0,N-1,0,N-1)
