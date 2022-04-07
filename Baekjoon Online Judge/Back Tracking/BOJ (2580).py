from sys import stdin

s_list=[list(map(int,stdin.readline().split())) for _ in range(9)]
check_blank=[]

for i in range(9):
    for j in range(9):
        if s_list[i][j] == 0:
            check_blank.append([i,j])

def check_row(x,p): #해당 행에 같은 숫자가 있는지 탐색하는 함수
        if p in s_list[x]:
            return False
        else:
            return True
def check_col(x,p): #해당 열에 같은 숫자가 있는지 탐색하는 함수
    for i in range(9):
        if s_list[i][x] == p:
            return False
    return True
def check_box(x,y,p):   #해당 3*3의 박스안에 같은 숫자가 있는지 탐색하는 함수
    nx=x//3*3
    ny=y//3*3
    for t in range(3):
        for f in range(3):
            if s_list[nx+t][ny+f] == p:
                return False
    return True

def bfs(l): #스도쿠를 완성하는 함수
    if l == len(check_blank):   #빈칸을 다 넣어 통과되었을 때 완료된 스도쿠를 출력
        for idx in range(9):
            print(*s_list[idx])
        exit(0)
    x=check_blank[l][0]
    y=check_blank[l][1]
    for i in range(1,10):   #빈칸에 i를 1부터 9까지 대입하면서 값을 삽입
        if check_row(x,i) and check_col(y,i) and check_box(x,y,i):
            s_list[x][y]=i
            bfs(l+1)
            s_list[x][y]=0  #blank가 만족하지 않았을 때 다시 돌아와서 0으로 초기화
            
bfs(0)