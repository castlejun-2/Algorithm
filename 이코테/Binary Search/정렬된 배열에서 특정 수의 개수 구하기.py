from sys import stdin

N,x=map(int,stdin.readline().strip().split())
number_list=list(map(int,stdin.readline().strip().split()))

def first_idx_binary_search(start,end,target):  #target의 값을 갖는 첫번째 idx를 구하는 함수
    if start > end:
        return -1
    mid=(start+end)//2
    if (mid==0 or number_list[mid-1]<target) and number_list[mid]==target:  #number_list[mid]와 target의 값이 일치하고, mid의 index보다 -1 작은 값이 target보다 작으면 return
        return mid
    if number_list[mid] >= target:  #number_list[mid]가 target보다 갖거나 크면 end 값을 줄여나간다.
        return first_idx_binary_search(start,mid-1,target)
    else:
        return first_idx_binary_search(mid+1,end,target)
    
def last_idx_binary_search(start,end,target):   #target의 값을 갖는 마지막 idx를 구하는 함수
    mid=(start+end)//2
    if (mid==N-1 or number_list[mid+1]>target) and number_list[mid]==target:    #number_list[mid]와 target의 값이 일치하고, mid의 index보다 +1 큰 값이 target보다 크면 return
        return mid
    if number_list[mid] > target:   
        return last_idx_binary_search(start,mid-1,target)
    else:   #number_list[mid]가 target보다 작거나 같으면 start 값을 키워나간다.
        return last_idx_binary_search(mid+1,end,target)

start_idx=first_idx_binary_search(0,N-1,x)
if start_idx==-1:
    print(-1)
else:
    last_idx=last_idx_binary_search(0,N-1,x)
    print(last_idx-start_idx+1)

        