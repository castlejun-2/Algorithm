import sys
input=sys.stdin.readline

N=int(input())
crane=sorted(list(map(int,input().split())),reverse=True)
M=int(input())
box=sorted(list(map(int,input().split())),reverse=True)
box_len=len(box)
time=0
count=0

boxIdx=[0]*N          #크래인의 현재 운반할 박스 Index
visited=[0]*M         #박스의 방문여부

if crane[0]<box[0]:
    print(-1)
else:
    while count<box_len:    #박스를 다 옮겼으면 반복 종료
        for i in range(N):  #모든 크레인을 작동
            while boxIdx[i]<box_len:                                      #처리 가능한 박스가 나올때 까지 반복
                if not visited[boxIdx[i]] and box[boxIdx[i]]<=crane[i]:   #박스가 아직 들리지 않았고, 들수 있으면
                    visited[boxIdx[i]]=1                                  #박스 방문처리
                    boxIdx[i]+=1                                          #다음 박스로 Index 이동
                    count+=1
                    break
                boxIdx[i]+=1                                              #처리가능한 박스가 없었다면, 다음 박스로 이동
        time+=1
    print(time)
