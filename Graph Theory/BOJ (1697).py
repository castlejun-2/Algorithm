from sys import stdin
from collections import deque

N,K=map(int,stdin.readline().split())
g_list=[0]*100001

def bfs():
    dq=deque()
    dq.append(N)
    while dq:
        x=dq.popleft()  #deque에 들어 있는 가장 앞의 값부터 검사하여준다.
        if x==K:
            print(g_list[x])
            return
        for loc in (x-1,x+1,x*2): #현재 위치 x에서 이동가능한 위치
            if 0<=loc<=100000 and not g_list[loc]:  #loc이 범위에 있고, g_list[loc]의 점에 도달 하지 못한 값들만 수정
                g_list[loc]=g_list[x]+1 #만약 g_list[loc]이 이미 존재한다면 해당 위치가 최소값 이므로 수정하지 않는다.
                dq.append(loc)
bfs() #넓이 우선 탐색 시작
