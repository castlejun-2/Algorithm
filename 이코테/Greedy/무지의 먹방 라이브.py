from sys import stdin
from collections import deque
import heapq

food_times=list(map(int,stdin.readline().split()))
K=int(stdin.readline())

def solution(food_times,K): #개인 풀이(정확성 통과, 효울성 실패)
    k=0
    dq=deque()
    for idx,time in enumerate(food_times):
        dq.append([time,idx])
    while k!=K and dq: #더 이상 먹을 음식이 없거나, 시간이 다 된다면 종료
        t,i=dq.popleft()
        if t:
            dq.append([t-1,i])
            k+=1
    if dq:  #시간이 종료된 경우, 남은 음식에서 먹을 음식 출력
        while True:
            time,idx=dq.popleft()
            if time:
                return idx+1
            else:
                continue
    else:   #시간이 종료되고, 남은 음식도 없을 경우 -1 출력
        return -1

def heapq_solution(food_times,K):   #heapq를 사용한 효율성 정답 solution
    if sum(food_times) <=K: #총 음식을 먹는데 걸리는 시간이 K초 보다 작거나 같으면 -1
        return -1
    
    q=[]
    food_length=len(food_times) #음식의 길이
    
    for i in range(food_length):
        heapq.heappush(q,(food_times[i],i+1))
    
    sum_value=0
    previous=0
    
    while sum_value + ( (q[0][0] - previous) * food_length) <= K:   # sum_value + (현재의 음식시간 - 이전 음식시간) * 현재 음식시간 <= K 비교
        now=heapq.heappop(q)[0] #가장 적게 남은 음식을 pop
        sum_value+=(now - previous) * food_length
        food_length-=1  #음식 하나를 다 먹었으므로 제외 시킨다.
        previous=now    #이전 음식의 시간을 재 설정한다.
    result=sorted(q,key=lambda x:x[1])
    return result[(K-sum_value) % food_length][1]
    
print(solution(food_times,K))
print(heapq_solution(food_times,K))