from sys import stdin

N,M=map(int,stdin.readline().split())
A_list=[list(map(int,stdin.readline().rstrip())) for _ in range(N)]
B_list=[list(map(int,stdin.readline().rstrip())) for _ in range(N)]
cnt=0

def ReverseMatrix(A,startX,startY):                         #3*3 matrix를 뒤집는 함수
    for i in range(3):
        for j in range(3):
            A[i+startX][j+startY]=1-A[i+startX][j+startY]
            
try:                                                        # 불필요한 반복을 줄이기 위해 행렬을 확인하였을 때 같으면 Error를 일으켜 원하는 값 출력 후 종료
    for i in range(N-2):                                    # N*M 행렬에서 3*3으로 뒤집을 수 있는 시작점은 열은 행은 N-2까지, 열은 M-2까지이다.
        for j in range(M-2):  
            if A_list[i][j]!=B_list[i][j]:                  # 3*3의 전체행렬이 뒤집혀야 하므로 3*3 행렬의 첫번째 행, 첫번째 열의 값만 확인해주고 같지 않으면 뒤집어준다.
                ReverseMatrix(A_list,i,j)
                cnt+=1
            if A_list==B_list:                              # 행렬이 같다면 Error를 일으켜 예외처리
                raise NotImplementedError
    if A_list==B_list:                                      # N,M 이 3보다 작은데, A와 B행렬이 같을 경우 Error처리로 넘어가주지 못해서 반복문이 끝났을 때 예외처리를 해주었다.
        print(0)            
    else:
        print(-1)
except:
    print(cnt)
