from sys import stdin

N,M=map(int,stdin.readline().strip().split())
nuddle_list=list(map(int,stdin.readline().strip().split()))

nuddle_list.sort(reverse=True)
answer=0
start=0;end=nuddle_list[0]

while start <= end:
    mid=(start+end)//2
    temp_total=0
    for nuddle in nuddle_list:  
        if nuddle <= mid:   #떡의 길이가 정렬되어 있으므로, 떡이 더 이상 안잘린다면 반복을 중지한다.
            break
        temp_total+=nuddle-mid
    if temp_total < M:  #절단된 떡의 길이가 가져가야 할 떡의 길이보다 작다면, 높이를 낮춰 떡을 더 많이 자른다.
        end=mid-1
    else:
        answer=mid  #가져갈 수 있는 떡의 길이 중 가장 짧아야 하므로 값을 저장시킨다.
        start=mid+1
print(answer)