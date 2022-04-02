import sys
sys.setrecursionlimit(10000) #재귀함수의 깊이를 더 할당해주기 위한 module 선언

dx=[0, 0,1,1, 1,-1,-1,-1]
dy=[1,-1,0,1,-1, 1, 0,-1]

def DFS(i,j):                #깊이 우선 탐색을 통해 연결되어 있는 1(땅)을 모두 방문
    m_list[i][j]=0           #방문한 땅은 0으로 수정
    for k in range(8):
        x=i+dx[k]
        y=j+dy[k]
        if 0<=x<b and 0<=y<a and m_list[x][y]==1: #범위내에 있으며 땅을 밟았으면 주변의 땅들을 더 탐색
            DFS(x,y)

if __name__=="__main__":            
    while True:
        a,b=map(int,input().split())
        if a==0 and b==0: #반복문 종료 조건
            break
        cnt=0
        m_list = [list(map(int,input().split())) for _ in range(b)] #2차원 배열의 값 받기
        for h in range(a):
            for w in range(b):
                if m_list[w][h]==1:
                    DFS(w,h)
                    cnt+=1  #주변 1(땅)의 탐색이 끝났다면 땅의 갯수 +1 증가
        print(cnt)  #현재 테스트 케이스의 땅의 갯수를 출력후 다음 반복 실행
