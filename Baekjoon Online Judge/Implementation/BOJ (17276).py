import copy
from sys import stdin

def rotate(N):
    tmp=[]
    global arr
    for i in range(N):
        tmp.append(arr[i][N//2])
    for i in range(N):  #1번 연산
        arr[i][N//2]=arr[i][i]
    for i in range(N):  #2번 연산
        arr[i][i]=arr[N//2][i]
    for i in range(N):  #3번 연산
        arr[N//2][i]=arr[N-1-i][i]
    for i in range(N):  #4번 연산
        arr[i][N-1-i]=tmp[i]
    return arr
    
T=int(stdin.readline())

for _ in range(T):
    n,angle=map(int,stdin.readline().split())
    arr=[list(map(int,stdin.readline().split())) for _ in range(n)]
    angle=(angle+360)%360 #음수를 양수횟수로 처리
    tmp=[]
    for _ in range(angle//45):  #갯수만큼 회전
        rotate(n)
    for i in range(n):
        print(" ".join(map(str,arr[i])))
