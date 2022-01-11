from sys import stdin

N,B=map(int,stdin.readline().split())

A_list=[list(map(int,stdin.readline().split())) for _ in range(N)]

def divide(A,B):                                          #divide 함수를 통하여 A->A^2->A^4... or A->A^2->A^2*A=A^3->A^6 의 순으로 계산해 나아갈 수 있다.
    if B==1:
        tmp_list=[[0]*N for _ in range(N)]                #B==1이라면 A에 1000을 나눈 나머지로 변환하여 돌려준다.
        for i in range(N):
            for j in range(N):
                A[i][j]%=1000
        return A     
    elif B%2==1:                                          #A^(2k+1) = (A^k)^2*A 이므로 ex)A^9 이라면 A^8을 구해준 후 A를 곱해준다.
        tmp_list=[[0]*N for _ in range(N)]
        C=divide(A,B-1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp_list[i][j]+=C[i][k]*A[k][j]
                tmp_list[i][j]%=1000
        return tmp_list
    else:                                                 #A^2k = (A^k)^2 이므로 ex)A^8 이라면 A^4*A^4을 하여준다.
        tmp_list=[[0]*N for _ in range(N)]
        C=divide(A,B//2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp_list[i][j]+=C[i][k]*C[k][j]
                tmp_list[i][j]%=1000
        return tmp_list
        
mul_list=divide(A_list,B)
for i in mul_list:
    print(" ".join(map(str,i)))
