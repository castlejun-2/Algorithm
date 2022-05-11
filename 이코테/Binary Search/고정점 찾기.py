from sys import stdin

N=int(stdin.readline().strip())
a=list(map(int,stdin.readline().strip().split()))

def binary_search(start,end):
    if start>end:
        return -1
    mid=(start+end)//2
    if a[mid]==mid:
        return mid
    elif a[mid]>mid:    #a[mid]가 mid보다 크면 mid 뒤의 idx는 절대 자기 자신과 같은 값을 가질 수 없다.
        return binary_search(start,mid-1)
    else:   #a[mid]가 mid보다 작으면 mid 이전의 idx는 절대 자기 자신과 같은 값을 가질 수 없다.
        return binary_search(mid+1,end)

print(binary_search(0,N-1))