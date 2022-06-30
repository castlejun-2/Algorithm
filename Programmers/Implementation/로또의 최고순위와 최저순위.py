def solution(lottos, win_nums):
    cnt=0
    zero=lottos.count(0)
    answer=[6,6]
    for lotto in lottos:    #확률이 가능한 번호 갯수
        if lotto in win_nums: #맞는 번호 갯수
            cnt+=1
    #하나도 맞는 것이 없다면 7등이 아닌 6등이 되어야 하므로 최소값은 6으로 고정한다.
    answer[0]=min(answer[0],7-(cnt+zero))   #7-(최대 가능성 갯수)는 등수가 된다.
    answer[1]=min(answer[1],7-cnt)  #7-맞은 갯수는 등수가 된다.
    return answer

def reservedsolution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]