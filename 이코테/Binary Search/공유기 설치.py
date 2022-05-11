from sys import stdin

N,C=map(int,stdin.readline().strip().split())
home=[]
for i in range(N):
    home.append(int(stdin.readline().strip()))
home.sort()

start=1
end=home[-1]-home[0]
answer=0

while start<=end:   #최대 가능한 gap은 10억이므로, 이 gap을 logN의 시간으로 줄여 나아간다.
    mid=(start+end)//2  #가능한 gap은 최소 1에서 최대 home[-1]-home[0] 이므로 그 중간의 mid를 gap으로 설정한다.
    now_location=home[0]
    cnt=1
    for i in range(1,N):    #앞의 값부터 검사하면서 gap이 mid라고 가정 했을 때, C개의 공유기가 설치가능한지 확인한다.
        if home[i]>=now_location+mid:
            now_location=home[i]
            cnt+=1
    if cnt>=C:  #gap이 mid일 때 C개의 공유기가 설치가능하다면 정답 값을 갱신한다.
        answer=mid  #이 때, mid 값은 증가하거나 감소하는 방식이므로, 갱신될 때 마다 가능한 최대값이 된다.
        start=mid+1
    else:
        end=mid-1   #gap이 Mid일 때 C의 공유기가 설치불가능하다면, 가능한 최대 gap은 현재 mid에서 -1을 해준 값으로 갱신해준다.
        
print(answer)