key=[[0,0,0],[1,0,0],[0,1,1]]
lock=[[1,1,1],[1,1,0],[1,0,1]]

def rotate(key):    #회전
    return list(zip(*key[::-1]))
def check_key(n_lock):  #lock과 key를 더하면 1이 됨을 확인
    lock_length=len(n_lock)//3
    for i in range(lock_length,lock_length*2):
        for j in range(lock_length,lock_length*2):
            if n_lock[i][j]!=1:
                return False
    return True
                
def solution(key, lock):
    N=len(lock)
    M=len(key)
    
    n_lock=[[0]*(N*3) for _ in range(N*3)]  #key가 튀어나가도 됨으로 자물쇠의 첫번째 부터 확인
    
    for i in range(N):
        for j in range(N):
            n_lock[N+i][N+j]=lock[i][j]
    
    for dir in range(4):
        key=rotate(key)
        for x in range(1,N*2):    
            for y in range(1,N*2):
                #자물쇠에 열쇠를 하나씩 맞춰본다
                for i in range(M):  
                    for j in range(M):  
                        n_lock[x+i][y+j]+=key[i][j]
                if check_key(n_lock):   #열쇠구멍이 일치한지 확인
                    return True
                for i in range(M):  #일치하지 않으면 원상복구
                    for j in range(M):
                        n_lock[x+i][y+j]-=key[i][j]
    return False

print(solution(key,lock))
