import sys
from itertools import combinations
import copy

N=int(sys.stdin.readline().strip())
SOT_list=[list(map(str,sys.stdin.readline().strip().split())) for _ in range(N)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(i,j,direction,sot): #Student들의 상하좌우에 선생님들의 감시영역에 걸리는지 확인
    if 0<=i<N and 0<=j<N:
        if sot[i][j]=='O':
            return True
        elif sot[i][j]=='T':
            return False
        else:
            nx=i+dx[direction]
            ny=j+dy[direction]
            return dfs(nx,ny,direction,sot)
    else:
        return True

def check(sot_list):    #Student들이 안전한지 확인하는 함수
    for x,y in S_list:
        for i in range(4):
            if dfs(x,y,i,sot_list):
                continue
            else:
                return False
    return True
        
O_list=[]
S_list=[]
YN=False

for i in range(N):
    for j in range(N):
        if SOT_list[i][j]=='X':
            O_list.append([i,j])
        elif SOT_list[i][j]=='S':
            S_list.append([i,j])

for predict in list(combinations(O_list,3)):    #N은 6보다 작으므로 전체탐색이 가능하다
    temp_SOT_list=copy.deepcopy(SOT_list)
    for x,y in predict: 
        temp_SOT_list[x][y]='O'
    if check(temp_SOT_list):    #한가지 경우라도 성공한다면 YN을 True로 바꾼 후 반복문 탈출
        YN=True
        break
if YN:  #성공 한 경우만 존재하면 YES
    print("YES")
else:   #존재하지 않는다면 NO
    print("NO") 
