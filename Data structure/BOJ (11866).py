from collections import deque

N,K=map(int,input().split())
y_list=[i for i in range(1,N+1)]    #요세푸스 list에 1부터 N까지 값 입력
dq=deque(y_list)                    #리스트를 deque에 삽입

print('<',end="")
while dq:                           #deque이 빌 때 까지 반복
    for i in range(K-1):            #K번째 앞 까지의 값들을 삭제 후 deque의 뒤에 삽입
        dq.append(dq[0])            #앞의 값을 뒤에 삽입
        dq.popleft()                #앞의 값을 삭제
    print(dq.popleft(),end="")      #K번째 값을 출력 후 삭제
    if dq:
        print(", ",end="")          #dq에 비어 있지 않다면 ','로 이어붙혀서 계속 출력
print('>')                          #dq가 다 비어있어 출력 종료
