from sys import stdin

def d_c(x,y,n):
    if n==2:    #n==2에 도달 시 해당 범위에서 두번째로 큰 값 return
        temp=[]
        for i in range(2):
            for j in range(2):
                temp.append(n_list[x+i][y+j])
        temp.sort(reverse=True)
        return temp[1]
    else:   #그 외에 각 부분구역으로 분할 하여 각 구역에서 두번째로 큰 값들을 계속해서 분류 후 마지막 병합과정에서의 두번째로 큰 값 추출 후 출력
        temp=[]
        temp.append(d_c(x,y,n//2))
        temp.append(d_c(x+n//2,y,n//2))
        temp.append(d_c(x,y+n//2,n//2))
        temp.append(d_c(x+n//2,y+n//2,n//2))
        temp.sort(reverse=True)
        return temp[1]

N=int(stdin.readline())
n_list=[list(map(int,stdin.readline().split())) for _ in range(N)]
print(d_c(0,0,N))
