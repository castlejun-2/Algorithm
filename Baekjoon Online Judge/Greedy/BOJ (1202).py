from sys import stdin
import heapq

N,K = map(int,stdin.readline().split())
j_list = []
sum = 0

for _ in range(N):
    heapq.heappush(j_list,list(map(int,stdin.readline().split())))
max_C = [int(stdin.readline().strip()) for _ in range(K)]

j_list.sort()
max_C.sort()

temp_j = []
for i in max_C:                                               #보석 list를 한번만 탐색하기 때문에 전체 시간은 O(N)이 소요된다.
        while j_list and (i >= j_list[0][0]):                 #가장 작은 가방부터 채워 넣는데, 무게에 맞는 보석들의 정보를 먼저 수집한다.
            heapq.heappush(temp_j,-heapq.heappop(j_list)[1])
        if temp_j:
            sum-=heapq.heappop(temp_j)                        #가방에 들어갈 수 있는 무게중 가장 비싼 금액의 보석을 채워넣는다.
print(sum)
