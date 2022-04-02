import sys
import heapq
input=sys.stdin.readline

if __name__=="__main__":
    heap=[]
    N=int(input())
    for i in range(N):
        x=int(input())
        if x==0:
            if len(heap)==0:                      #길이가 0이고 입력된 값이0이면 0을 
                print(0)
            else:
                print(-(heapq.heappop(heap)))     #파이썬은 최소힙을 지원하므로, -가 곱해져 최소값으로 들어가있는 값을 다시 -를 곱해 원래 입력된 값으로 출력하여준다.
        else:
            heapq.heappush(heap,-x)               #파이썬은 최소힙을 지원하므로, -를 곱해 값을 넣어준다
