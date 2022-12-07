def solution(sticker):
    n = len(sticker)
    if n <= 3:
        return max(sticker)
    
    dp_0 = [0] * n
    dp_1 = [0] * n
    
    #첫번째 스티커를 제거한 경우
    dp_0[0] = sticker[0]    
    dp_0[1] = dp_0[0]       #두번째 스티커는 사용하지 못한다.
    
    for i in range(2,n-1):  #마지막 스티커는 사용하지 못한다.
        dp_0[i]=max(dp_0[i-1],dp_0[i-2]+sticker[i]) #i번째 스티커를 제거안한 경우 vs 제거한 경우

    #첫번째 스티커를 제거하지 않은 경우
    for i in range(1,n):
        dp_1[i]=max(dp_1[i-1],dp_1[i-2]+sticker[i]) #i번째 스티커를 제거안한 경우 vs 제거한 경우
    
    return max(dp_0[n-2],dp_1[n-1])
