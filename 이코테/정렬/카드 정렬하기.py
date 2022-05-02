import heapq

N=int(input())
card_list=[]

for i in range(N):
    card=int(input())
    heapq.heappush(card_list,card)  #heapq module을 통해, 작은 수들부터 더해 나아갈 때 항상 리스트가 오름차순을 유지 할 수 있도록 해준다.
answer=0

while len(card_list) > 1:
    temp_card_1=heapq.heappop(card_list)   
    temp_card_2=heapq.heappop(card_list)
    answer+=(temp_card_1+temp_card_2)
    heapq.heappush(card_list,temp_card_1+temp_card_2)

print(answer)
