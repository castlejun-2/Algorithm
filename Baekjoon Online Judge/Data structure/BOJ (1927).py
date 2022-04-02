
import sys
import heapq
input=sys.stdin.readline

if __name__=="__main__":
    heap=[]
    N=int(input())
    for i in range(N):
        x=int(input())
        if x==0:
            if len(heap)==0:
                print(0)
            else:
                print(heapq.heappop(heap))  #x는 0이고, heap이 비어있지 않을 때, 가장 작은 root 값을 출력 후 pop
        else:
            heapq.heappush(heap,x)          #입력받은 x값을 heap
