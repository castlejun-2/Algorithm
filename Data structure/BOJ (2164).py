import sys
from collections import deque     #덱(deque) 사용을 위한 library 사용
input=sys.stdin.readline

N=int(input())                    #N값을 받아 int형으로 변환 
card=deque()                      #덱(deque) 객체를 card 변수로 선언
for i in range(N):                #덱(deque)에 초기값 append
    card.append(i+1)
    
while(len(card)>1):               #card의 길이가 1이 될 때 까지 카드를 버리고 섞는 과정을 반복
    card.popleft()
    card.append(card.popleft())

print(card.popleft())
#시간복잡도적인 측면에서 상당히 손해를 보도록 풀어버린 문제이다. 나의 해답 외에 다른 해답을 찾아보았는데 문제의 규칙을 찾아내 시간복잡도를 거의 1/5 가량 줄인 코드도 보았다. 한 방향으로만 푸려는 습관을 고쳐야겠다.
