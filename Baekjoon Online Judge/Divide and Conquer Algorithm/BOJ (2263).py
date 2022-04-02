import sys
from sys import stdin
sys.setrecursionlimit(10**9)

def preorder(in_start,in_end,post_start,post_end):
    if(in_start>in_end) or (post_start>post_end): return

    p_index=post_list[post_end] #후위순회의 마지막 값이 서브트리의 루트임을 이용
    print(p_index, end=" ")
    
    #중위순회에서 값이 좌 우로 갈라짐을 이용
    left=index[p_index]-in_start    
    right=in_end-index[p_index]
    
    preorder(in_start,in_start+left-1,post_start,post_start+left-1) #왼쪽 서브트리
    preorder(in_end-right+1,in_end,post_end-right,post_end-1)       #오른쪽 서브트리

N=int(stdin.readline())
in_list=list(map(int,stdin.readline().split()))     #중위순회 값
post_list=list(map(int,stdin.readline().split()))   #후위순회 값
index=[0]*(N+1)

for i in range(N):      #중위순회의 값이 갖는 index위치를 표현
    index[in_list[i]]=i

preorder(0,N-1,0,N-1)
