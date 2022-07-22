from sys import stdin

N=int(stdin.readline())
calendar=[0]*366
width=0     #넓이
height=0    #높이
answer=0

for _ in range(N):
    start,end=map(int,stdin.readline().split())
    for i in range(start,end+1):    #해당하는 요일에 일정 갯수 추가
        calendar[i]+=1

for i in range(len(calendar)):
    if calendar[i]: #일정이 있다면 넓이와 높이 변경
        if height < calendar[i]:    #해당 일정의 높이가 기존 높이보다 높다면
            height=calendar[i]  #높이 변경
        width+=1
    else:   #일정이 없는 구간이 등장한다면
        answer+=width*height    #누적되어 있던 넓이를 answer에 추가
        width=0     #넓이 초기화
        height=0    #높이 초기화

answer+=width*height    #마지막날까지 일정이 있을 경우 예외처리
print(answer)
