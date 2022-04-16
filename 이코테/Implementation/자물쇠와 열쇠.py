key=[[0,0,0],[1,0,0],[0,1,1]]
lock=[[1,1,1],[1,1,0],[1,0,1]]

def rotate(key):
    return list(zip(*key[::-1]))
def check_key(n_lock):
    lock_length=n_lock//3
    for i in range(lock_length,lock_length*2):
        for j in range(lock_length,lock_length*2):
            if n_lock[i][j]!=1:
                return False
    return True
                
def solution(key, lock):
    N=len(lock)
    M=len(key)
    
    n_lock=[[0]*(N*3) for _ in range(N*3)]
    
    for i in range(N):
        for j in range(N):
            n_lock[N+i][N+j]=lock[i][j]
