from collections import deque

N,M = map(int,input().split())
p_list = list(map(int,input().split()))
dq = deque([i for i in range(1,N+1)])
cnt = 0

for i in p_list:
    while True:
        if dq[0] == i:                          #현재 dq의 가장 앞의 원소와 내가 뽑으려했던 i가 같으면 1번 연산 수행
            dq.popleft()
            break
        else:
            if dq.index(i) <= len(dq)/2:        #뽑으려 하였던 i의 현재 dq에서의 index가 현재 dq의 길이의 1/2배보다 짧거나 같으면 앞의 숫자를 뒤로 이동 (2번 연산)
                while dq[0] != i:               #뽑으려는 원소가 dq의 가장 앞에 오면 반복 중지
                    dq.append(dq.popleft()) 
                    cnt += 1
            else:                               #뽑으려 하였던 i의 현재 dq에서의 index가 현재 dq의 길이의 1/2배보다 길면 뒤의 숫자를 앞으로 이동 (3번 연산)
                while dq[0] != i:               #뽑으려는 원소가 dq의 가장 앞에 오면 반복 중지
                    dq.appendleft(dq.pop())
                    cnt += 1
print(cnt)
