def check_area(x,y,n):                      #영역이 모두 같은 숫자로 이루어져있는지 검증
    tmp=m_list[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if tmp!=m_list[i][j]:
                return False
    return True

def divide(x,y,n):
    if check_area(x,y,n):                   #영역이 같은 숫자로 이루어져있으면 해당 영역의 가장 앞의 값에 +1
        result[m_list[x][y]+1]+=1
    else:                                   #영역에 다른 숫자가 있다면 9개의 영역으로 나누어 다시 탐색
        for i in range(3):
            for j in range(3):
                divide(x+i*(n//3),y+j*(n//3),n//3)  
    return
  
if __name__=="__main__":
    N=int(input())
    m_list=[list(map(int,input().split())) for _ in range(N)]
    result=[0]*3

    divide(0,0,N)                            #(0,0)부터 
    for i in range(3):
        print(result[i])
