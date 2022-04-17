from itertools import combinations
from sys import stdin
import copy

def cal_distance(x1,y1,x2,y2):  #거리를 계산하는 함수
    return abs(x1-x2)+abs(y1-y2)

def cal_home_distance(x,y): #치킨집에서의 각 집의 거리를 계산
    for i in range(N):
        for j in range(N):
            if city_list[i][j]==1:
                temp_distance=cal_distance(x,y,i,j) #해당 위치의 치킨집이 최소거리라면, 해당 집에서 가장 가까운 치킨집이므로 값 update
                if temp_distance < distance[i][j]:
                    distance[i][j]=temp_distance

N,M=map(int,stdin.readline().split())
city_list=[list(map(int,stdin.readline().split())) for _ in range(N)]
chicken_list=[]

for i in range(N):  #치킨집이 위치하는 좌표를 삽입
    for j in range(N):
        if city_list[i][j]==2:
            chicken_list.append([i,j])
            
temp_index=list(combinations(chicken_list,len(chicken_list)-M)) #combinatino 함수를 통해 치킨 집 위치를 특정
min_result=4900 #N은 최대 50이므로 N=50일 때 각 집은 최대 98의 거리를 갖게됨. 따라서 98*50 을 통해 min_result 의 최대값을 설정
if temp_index:  #존재하는 치킨집이, 남겨야 할 치킨집의 갯수보다 많은 경우
    for temp in temp_index:
        distance=[[2*N-2]*N for _ in range(N)]
        temp_sum=0
        temp_city=copy.deepcopy(city_list)

        for t in temp:
            a,b=t
            temp_city[a][b]=0
        for i in range(N):  #치킨집을 만났을 때, 각 치킨집에 대한 집들의 거리를 계산
            for j in range(N):
                if temp_city[i][j]==2:
                    cal_home_distance(i,j)
        for i in range(N):  #위에서 각 치킨집에 대한 거리가 계산되었으므로, 각 집들의 치킨거리의 합산
            for j in range(N):
                if temp_city[i][j]==1:
                    temp_sum+=distance[i][j]
        min_result=min(temp_sum,min_result) #현재 치킨집들이 남았을 때의 치킨거리의 합과, 기존 치킨거리의 합중 최솟값 대입
else:   #존재하는 치킨집과, 남겨야 하는 치킨집의 갯수가 같은 경우
    distance=[[2*N-2]*N for _ in range(N)]
    temp_sum=0
    for i in range(N):
            for j in range(N):
                if city_list[i][j]==2:
                    cal_home_distance(i,j)
            for i in range(N):
                for j in range(N):
                    if city_list[i][j]==1:
                        temp_sum+=distance[i][j]
    min_result=min(temp_sum,min_result)
print(min_result)
