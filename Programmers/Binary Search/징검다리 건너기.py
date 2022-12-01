def solution(stones, k):
    answer = 0
    left = 0
    right = max(stones)
    
    while left <= right:
        mid = (left+right)//2
        cnt_0 = 0
        for stone in stones:
            if stone - mid < 0:
                cnt_0 += 1
            else:
                cnt_0 = 0
            if cnt_0 >= k:        #연속된 0이 k개 이상이면 종료
                break
        if cnt_0 >= k:            #연속된 0이 k개 이상이면, mid명 만큼 징검다리를 건너지 못하는것이므로 범위 축소
            right = mid - 1
        else:                     #mid명 만큼 징검다리를 건넜다면, 더 건널 수 있는지 확인하기 위해 범위 
            left = mid + 1
    
    return right
