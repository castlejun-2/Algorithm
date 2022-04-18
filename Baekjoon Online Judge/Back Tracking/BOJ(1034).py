# 모든 행에 접근해서 switch를 해주고, 행을 검사하므로 시간초과 발생
# from sys import stdin
# import copy
# import sys
# sys.setrecursionlimit(2500)

# def check_line(arr):
#     if 0 in arr:
#         return False
#     return True

# def switch(arr,i):
#     temp_list=copy.deepcopy(arr)
#     for k in range(N):
#         temp_list[k][i]=(temp_list[k][i]-1)%2
#     return temp_list

# def dfs(arr,idx):
#     if idx==K:
#         global max_cnt
#         cnt=0
#         for i in range(N):
#             if check_line(arr[i]):
#                 cnt+=1
#         max_cnt=max(max_cnt,cnt)
#     else:
#         for k in range(M):
#             temp_arr=switch(arr,k)
#             dfs(temp_arr,idx+1)
    
# N,M=map(int,stdin.readline().split())
# lamp_list=[list(map(int,stdin.readline().strip())) for _ in range(N)]
# K=int(stdin.readline().strip())
# max_cnt=0

# dfs(lamp_list,0)
# print(max_cnt)

# 아래의 풀이 방법은 각 행을 비교하여 최종적으로 켜질 수 있는지의 여부를 판단 후 같은 값을 같는 행을 찾으므로
# 시간복잡도가 최대 O(NM^2) 이다. 이 때 N과 M은 최대 50 이므로 위의 방식보다 시간이 효율적이다.
from sys import stdin
import copy

def check_same_row(arr):
    global max_cnt
    cnt=0
    for lamp in lamp_list:
        if lamp==arr:
            cnt+=1
    max_cnt=max(max_cnt,cnt)

N,M=map(int,stdin.readline().split())
lamp_list=[list(map(int,stdin.readline().strip())) for _ in range(N)]
K=int(stdin.readline().strip())
max_cnt=0

for lamp in lamp_list:
    cnt_0=0
    for lp in lamp: #각 행의 0의 갯수를 샌다
        if lp:
            continue
        cnt_0+=1
    if cnt_0 > K:   #0의 갯수보다 스위치를 켤 수 있는 갯수가 적으면 해당 행은 불빛이 들어올 수 없다
        continue
    else:
        if cnt_0%2 != K%2:  #0의 갯수와 K의 홀수 짝수가 다르면, 해당 행은 불빛이 들어올 수 없다.
            continue
        else:
            check_same_row(lamp)    #그 외의 경우에는 불빛을 켤 수 있으므로 해당 행과 같은 행의 갯수를 찾는다.
print(max_cnt)


