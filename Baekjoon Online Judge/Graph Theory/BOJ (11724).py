import sys

sys.setrecursionlimit(10000)                  #파이썬의 기본 재귀함수 깊이는 1000으로 되어있어, 해당 답안의 시간초과로 인해 재귀깊이를 증가시켜주었다.

N,M = map(int,sys.stdin.readline().split())   #입력을 받는 속도가 input().split() 보다 sys.stdin.readline().split()이 더 빨라 수정해주었다.    
g_list = [[] for _ in range(N)]
visited = set()                               #visited를 list로 생성한다면 한번 확인시마다 O(N)의 시간이 걸려 해시를 사용하여 O(1)시간이 걸리는 set으로 설정해주었다.
cnt = 0

def dfs(v):
    visited.add(v)
    
    for i in g_list[v]:                       #g_list에서 방문되지 않은 정점을 찾아가 방문 표시를 하여준다.
        if i-1 not in visited:
            dfs(i-1)
    
for i in range(M):
    s,e = map(int,sys.stdin.readline().split())
    g_list[s-1].append(e)
    g_list[e-1].append(s)

for i in range(N):
    if i not in visited:
        dfs(i)                                #하나의 연결요소를 찾아준다.
        cnt+=1

print(cnt)
