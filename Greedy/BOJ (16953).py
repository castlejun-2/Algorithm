import sys
import collections
input=sys.stdin.readline
mincnt=[]

def Dfs(num,cnt):           #깊이 우선을 통하여 가능한 모든 경우의 수를 비교한다
    if(num>B):
        return
    if(num==B):
        mincnt.append(cnt)

    Dfs(num*2,cnt+1)        #1번 규칙: 2배 해주었을 때
    Dfs(num*10+1,cnt+1)     #2번 규칙: 끝 자리에 1을 더해주었을 때

if __name__ == "__main__":
    A,B=map(int, input().split())
    
    Dfs(A,1)
    if not mincnt:
        print(-1)
    else:
        print(min(mincnt))  #mincnt list중 가장 작은 값을 출력
        
# 깊이 우선탐색을 통해 가능한 모든 경우의 수를 살피고, 값이 같게 되었을 때의 cnt들을 비교하여 가장 작은 수를 출력하도록 구현        
