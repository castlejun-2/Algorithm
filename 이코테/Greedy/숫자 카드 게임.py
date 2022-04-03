from sys import stdin

N,M=map(int,stdin.readline().split())
card_list=[list(map(int,stdin.readline().split())) for _ in range(N)]
max_card=0

#각 행에서 가장 작은 값들 중 가장 큰 값을 추출
for card in card_list:  
    temp_max=min(card)
    max_card=max(temp_max,max_card)
print(max_card)