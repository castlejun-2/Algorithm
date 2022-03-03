from sys import stdin

def preorder(in_start,in_end,post_start,post_end):
    if(in_start>in_end) or (post_start>post_end): return

    p_index=post_list[post_end]
    print(p_index, end="")
    
    left=index[p_index]-in_start
    right=in_end-index[p_index]
    
    #재귀를 어떻게 돌릴것인가!

N=int(stdin.readline())
in_list=list(map(int,stdin.readline().split()))
post_list=list(map(int,stdin.readline().split()))
index=[0]*(N+1)

for i in range(N):
    index[in_list[i]]=i

preorder(0,N-1,0,N-1)
