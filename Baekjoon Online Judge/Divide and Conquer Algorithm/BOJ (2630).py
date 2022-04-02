white = 0
blue = 0

def divide(x,y,N):
    global white
    global blue
    c = m_list[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if c!=m_list[i][j]:             #범위 탐색중 다른 숫자가 있다면 범위를 2로 다시 분할
                divide(x,y,N//2)  
                divide(x+N//2,y,N//2)
                divide(x,y+N//2,N//2)
                divide(x+N//2,y+N//2,N//2)
                return    
    if c:                                   #탐색이 끝난 후 해당 컬러에 맞는 색종이의 색 +1
        white+=1;
    else:
        blue+=1
        
if __name__=="__main__":
    N = int(input())
    m_list=[list(map(int,input().split())) for _ in range(N)]
    divide(0,0,N)
    print(blue)
    print(white)
