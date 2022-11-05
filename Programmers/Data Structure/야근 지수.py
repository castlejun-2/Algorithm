import heapq

def solution(n, works):
    hq = []
    answer = 0
    for work in works:
        heapq.heappush(hq,-work)
    
    while n:  #최대힙에서 가장 큰 값에 -1을 해준다.
        heapq.heappush(hq,-(-heapq.heappop(hq)-1))
        n-=1
    
    while hq and hq[0]<0:   #최대값이 0보다 작거나 같다면 반복을 멈춘다.
        answer+=(-heapq.heappop(hq))**2
    
    return answer
