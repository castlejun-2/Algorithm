import copy
N,M = map(int,input().split())
m_list = [list(map(int,input().split())) for _ in range(N)]

v_list = []
max_safe = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(N):                #바이러스 위치를 먼저 저장
    for j in range(M):
        if m_list[i][j] == 2:
            v_list.append([i,j])

def choice_wall(start,count):     #벽을 세우기 위해 전체 탐색
    global max_safe
    if count == 3:
        copy_list = copy.deepcopy(m_list)
        for i in v_list:
            row,col = i
            go_virus(row,col,copy_list)                 #바이러스를 침투
        temp_max = sum(c.count(0) for c in copy_list)   #바이러스 침투 후 안전지대 count
        max_safe = max(max_safe,temp_max)               #현재 계산된 최대 안전지대와비교
        return True
    else:                                               #벽이 세워지지 않았다면
        for i in range(start,N*M):                      #벽을 choice
            row = i // M
            col = i % M
            if m_list[row][col] == 0:
                m_list[row][col] = 1
                choice_wall(i,count+1)
                m_list[row][col] = 0
                
def go_virus(row,col,c_list):
    for i in range(4):                                  #상하 좌우로 감염
        dr = row + dx[i]  
        dc = col + dy[i]
        if 0<=dr<N and 0<=dc<M:                         #안전지대라면 감염
            if c_list[dr][dc] == 0:
                c_list[dr][dc] = 2
                go_virus(dr,dc,c_list)

if __name__=="__main__":                
    choice_wall(0,0)
    print(max_safe)
