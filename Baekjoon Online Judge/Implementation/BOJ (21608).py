dx=[-1,0,0,1]
dy=[0,-1,1,0]

def findIdx(sno):
    idxStack=[] #주어진 조건에 만족하는 좌석을 담을 배열
    for i in range(N):
        for j in range(N):
            if not arr[i][j]:   #해당 값이 비어있는 경우만
                like=0  #좋아하는 학생 인접 수
                emp=0   #빈 공간 수
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<N and 0<=ny<N:
                        if not arr[nx][ny]: #비어 있는 공간 탐색
                            emp+=1
                        elif arr[nx][ny] in student[sno]:   #좋아하는 학생의 수 탐색
                            like+=1
                idxStack.append([i,j,emp,like])
    idxStack.sort(key=lambda x:(-x[3],-x[2],x[0],x[1])) #주어진 조건순으로 정렬
    return idxStack[0][0],idxStack[0][1]
    
N=int(input())
student={}
arr=[[0]*N for _ in range(N)]
answer=0

for _ in range(N**2):
    info=list(map(int,input().split()))
    student[info[0]]=info[1:5]
    x,y=findIdx(info[0])    #자신이 갈 수 있는 최적의 자리 탐색
    arr[x][y]=info[0]   #해당 좌석에 착석

for i in range(N):
    for j in range(N):
        tmpLike=0   #각 좌석에 인접한 학생 수 계산
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] in student[arr[i][j]]:   #각 좌석에 인접한 학생이 존재할 경우
                tmpLike+=1
        if tmpLike==4:
            answer+=1000
        elif tmpLike==3:
            answer+=100
        elif tmpLike==2:
            answer+=10
        elif tmpLike==1:
            answer+=1
print(answer)