from sys import stdin

N=int(stdin.readline().strip())
part_list=list(map(int,stdin.readline().strip().split()))
M=int(stdin.readline().strip())
check_part_list=list(map(int,stdin.readline().strip().split()))

#(N+M)logN 의 시간 발생 = 정렬시간 (N)*logN + 부품 찾는시간 (M)*logN

def binary_search(array,target,start,end):
    if start > end:
        return "no"
    mid=(start+end)//2
    if array[mid]==target:
        return "yes"
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)
    
part_list.sort()
for i in check_part_list:
    print(binary_search(part_list,i,0,N-1),end=" ")