N,r,c = map(int,input().split())

def find(row,col,N):
    if N==0:
        return 0
    else:
        return 2*(row%2)+(col%2)+4*find(row//2,col//2,N-1)  #좌표가 2배 증가할 때 값이 4배 증가한다. 이 때 2*(row%2)+(col%2)는 2*2 박스에서 자신의 증가분을 찾아주고,
                                                            #2*2의 첫번 째 값은 다시 자신을 4배 시킨 현재 좌표의 1/2 의 값을 찾아준다. 
print(find(r,c,N))                                          #다음과 같은 재귀 방식으로 값을 찾아 나아간다.
