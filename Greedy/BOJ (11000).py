from sys import stdin
import heapq

N=int(stdin.readline())
ST_list=[]

for _ in range(N):
    S,T=map(int,stdin.readline().split())
    ST_list.append([S,T])
ST_list.sort(key=lambda x:x[0])

room=[]
heapq.heappush(room, ST_list[0][1]) #회의 종료시간이 일찍 끝나는 회의부터 정렬하기 위해 최대힙 우선순위 큐 사용

for i in range(1,N):
    if room[0] > ST_list[i][0]: #가장 일찍 끝나는 회의시간보다 현재 진행하려는 회의의 시작시간이 빠른 경우 새로운 회의실 개방
        heapq.heappush(room, ST_list[i][1]) #회의가 끝나는 시간을 우선순위큐에 삽입
    else:
        heapq.heappop(room) #현재 종료 예정인 회의시간보다 늦게 회의가 시작하는 경우 현재 강의실의 회의 종료시간을 변경
        heapq.heappush(room, ST_list[i][1]) 
print(len(room))  #현재 개방되어 있는 회의실의 갯수 출력
