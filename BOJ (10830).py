from sys import stdin

N,B=map(int,stdin.readline().split())

A_list=[list(map(int,stdin.readline().split())) for _ in range(N)]

def divide(A,B):
    if B==1:
        tmp_list=[[0]*N for _in range(N)]
        for i in range(N):
            for j in range(N):
                A[i][j]%=1000
        return A     
    elif B%2==1:
        tmp_list=[[0]*N for _in range(N)]
        C=divide(A,B-1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp_list[i][j]+=C[i][k]*A[k][j]
                tmp_list%=1000
        return tmp_list
    else:
        tmp_list=[[0]*N for _in range(N)]
        C=divide(A,B//2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp_list[i][j]+=C[i][k]*C[k][j]
                tmp_list%=1000
        return tmp_list
        
divide(A_list,B)
