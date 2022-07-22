'dq의 rotate를 활용한 문제풀이'
from sys import stdin
from collections import deque

def rotate(idx,R):
    global arr
    for i in range(idx):    #테두리 영역의 두께만큼 반복
        dq=deque()
        #윗면 복사
        for k in range(i,M-i-1):
            dq.append(arr[i][k])
        #오른면 복사
        for k in range(i,N-i-1):    
            dq.append(arr[k][M-i-1])
        #아랫면 복사
        for k in range(M-i-1,i,-1):
            dq.append(arr[N-i-1][k])
        #왼쪽면 복사
        for k in range(N-i-1,i,-1):
            dq.append(arr[k][i])
        
        dq.rotate(-R)   #R만큼 회전
        
        #수정된 윗면 복사
        for k in range(i,M-i-1):
            arr[i][k]=dq.popleft()
        #수정된 오른면 복사
        for k in range(i,N-i-1):    
            arr[k][M-i-1]=dq.popleft()
        #수정된 아랫면 복사
        for k in range(M-i-1,i,-1):
            arr[N-i-1][k]=dq.popleft()
        #수정된 왼쪽면 복사
        for k in range(N-i-1,i,-1):
            arr[k][i]=dq.popleft()
            
N,M,R=map(int,stdin.readline().split())
arr=[list(map(int,stdin.readline().split())) for _ in range(N)]

rotate(min(N,M)//2,R)

for i in range(N):
    print(" ".join(map(str,arr[i])))
    
'배열값 복사를 통한 문제풀이(배열 복사로 인한 시간이 오래걸려 pypy에서만동작)'
from sys import stdin

def rotate(idx,R):
    for _ in range(R):
        global arr
        for i in range(idx):
            #상
            tmp=arr[i][i]
            for k in range(i,M-i-1):
                arr[i][k]=arr[i][k+1]
            #우
            for k in range(i,N-i-1):
                arr[k][M-i-1]=arr[k+1][M-i-1]
            #하
            for k in range(M-i-1,i,-1):
                arr[N-i-1][k]=arr[N-i-1][k-1]
            #좌
            for k in range(N-i-1,i,-1):
                arr[k][i]=arr[k-1][i]
            arr[i+1][i]=tmp
            
N,M,R=map(int,stdin.readline().split())
arr=[list(map(int,stdin.readline().split())) for _ in range(N)]

rotate(min(N,M)//2,R)

for i in range(N):
    print(" ".join(map(str,arr[i])))
